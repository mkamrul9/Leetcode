import sys

# sys.stdout = open('output.txt', 'w')
# sys.stdin = open('input.txt', 'r')

input = lambda: sys.stdin.readline().strip()
gi = lambda: int(input())
gmi = lambda: map(int, input().split())

t = gi()

for _ in range(t):
    n, k = gmi()
    s = input()
    
    if 2 * k > n:
        print(-1)
    else:
        ans = 0
        
        for i in range(k):
            if s[i] == 'L':
                ans += 1
                
        for i in range(n - k, n):
            if s[i] == 'R':
                ans += 1
                
        print(ans)