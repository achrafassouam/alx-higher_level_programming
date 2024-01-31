#!/usr/bin/python3
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

N = sys.argv[1]

try:
    N = int(N)
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4") 
    sys.exit(1)

def solveNQueens(n):
    solutions = []
    solve(n, [], solutions)
    return solutions

def solve(n, columnPlacement, solutions):
    if len(columnPlacement) == n:
        solutions.append(list(columnPlacement))
        return
    
    for i in range(n):
        if isSafe(columnPlacement, i):
            columnPlacement.append(i)
            solve(n, columnPlacement, solutions)
            columnPlacement.pop()
            
def isSafe(columnPlacement, i):
    row = len(columnPlacement)
    for queen in range(row):
        if columnPlacement[queen] == i or abs(columnPlacement[queen] - i) == row - queen:
            return False
    return True

for solution in solveNQueens(N):
    print([[i, solution[i]] for i in range(N)])
