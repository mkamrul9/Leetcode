import sys

# sys.stdout = open('output.txt', 'w')
# sys.stdin = open('input.txt', 'r')

input = lambda: sys.stdin.readline().strip()
gi = lambda: int(input())
gs = lambda: input().split()

t = gi()

for i in range(t):
    x_str = input()
    L = len(x_str)
    
    minwf = 10**L + 1
    
    print(minwf)