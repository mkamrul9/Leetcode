import sys

# sys.stdout = open('output.txt', 'w')
# sys.stdin = open('input.txt', 'r')

input = lambda: sys.stdin.readline().strip()
gi = lambda: list(map(int, input().split()))
gs = lambda: input().split()

t = int(input())

for i in range(t):
    n, k = gi()
    total_popcount = 0
    weight = 1
    
    while n >= weight:
        take = min(k, n // weight)
        total_popcount += take
        n -= take * weight
        weight *= 2
        
    print(total_popcount)