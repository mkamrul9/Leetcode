import sys

# sys.stdout = open('output.txt', 'w')
# sys.stdin = open('input.txt', 'r')

input = lambda: sys.stdin.readline().strip()
gi = lambda: int(input())

t = gi()

for _ in range(t):
    n = gi()
  
    ans = []

    for i in range(1, n + 1, 2):
        ans.append(i + 1)
        ans.append(i)
        
    print(*ans)