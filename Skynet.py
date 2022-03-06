import numpy as np
import time
import socket

def move(state, src, des, n):
    cur = state
    for i in range (0, n):
        pos = cur % 3 # vi tri cua dia i
        if des == pos:
            return state
        if src == pos:
            return state - pos * 3**i + des * 3**i
        cur = cur // 3
    return state

def toArray(state, n):
    arr = np.zeros(n, int)
    for i in range (0, n):
        arr[i] = state % 3
        state = state // 3
    return arr

def H(state, n):
    arr = toArray(state, n)
    iy = 0
    right = 0
    N = 0
    Y = 0
    Z = 0
    count = np.zeros(3, int)
    r = True
    for i in range (n-1, -1, -1):
        pos = arr[i]
        count[pos] += 1
        if r == True:
            if pos == 2:
                right+=1
            else:
                r = False
                N = n - right
                iy = pos
    Y = count[iy]
    Z = count[2] - right
    mN = 0
    if N == 0:
        mN = 1/2
    else:
        mN = 2**(N-1)
    mY = 0
    if Y == 0:
        mY = 1/2
    else:
        mY = 2**(Y-1)
    return mN + mY + 2**Z - 2

def getH(n):
    h = np.zeros(3**n)
    for i in range(0, 3**n):
        h[i] = H(i, n)
    return h
def children(state, n):
    c01 = move(state, 0, 1, n)
    c02 = move(state, 0, 2, n)
    c10 = move(state, 1, 0, n)
    c12 = move(state, 1, 2, n)
    c20 = move(state, 2, 0, n)
    c21 = move(state, 2, 1, n)
    return [c01, c02, c10, c12, c20, c21]

def HanoiTower(n):
    count = 0
    n3 = 3**n
    h = getH(n)
    g = np.array([-1 for i in range(0, n3)])
    initialState = np.random.randint(n3)
    g[initialState] = 0
    parent = np.array([-1 for i in range(0, n3)])
    close = np.array([False for i in range(0, n3)])
    open = np.array([10**n for i in range(0, n3)])
    open[initialState] = h[initialState]
    current = -1
    start = time.time()
    while(current != n3 - 1):
        current = open.argmin()
        if current == n3 - 1:
            break
        count+= 1

        if open[current] == n3:
            break
        open[current] = n3
        close[current] = True
        c = children(current, n)
        for i in range(0, 6):
            ci = c[i]
            if ci != current:
                if close[ci] == False:
                    if g[ci] == -1 | g[ci] > g[current] + 1:
                        g[ci] = g[current] + 1
                    fci = g[ci] + h[ci]
                    if fci < open[ci]:
                        parent[ci] = current
                        open[ci] = fci
    end = time.time()
    path = []
    while(current != -1):
        path.append(current)
        current = parent[current]
    for i in range(len(path) - 1, -1 , -1):
        arr.append(toArray(path[i], n) + 1)
    for i in range(len(arr) - 1):
        for k in range(n):
            if(arr[i][k] != arr[i+1][k]):
                array.append(arr[i][k])
                array.append(arr[i+1][k])
                continue