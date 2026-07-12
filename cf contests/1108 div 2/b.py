import sys

# sys.stdout = open('output.txt', 'w')
# sys.stdin = open('input.txt', 'r')

input = lambda: sys.stdin.readline().strip()
gi = lambda: int(input())

t = gi()

for _ in range(t):
    n = gi()
    
    if n == 1:
        print(1)
    elif n == 2:
        print(-1)
    else:
        ans = []
        
        for i in range(1, n - 1):
            ans.append(3 * (2 ** (n - 2 - i)))
        
        ans.append(2)
        ans.append(1)
        
        print(*ans)