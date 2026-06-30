import sys

# sys.stdout = open('output.txt', 'w')
# sys.stdin = open('input.txt', 'r')

input = lambda: sys.stdin.readline().strip()
gi = lambda: list(map(int, input().split()))
gs = lambda: input().split()

t = int(input())

for i in range(t):
    x, y = gi()
 
    if x % y == 0:
        print("YES")
    else:
        print("NO")