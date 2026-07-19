import sys

sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

input = lambda: sys.stdin.readline().strip()
gi = lambda: int(input())
gmi = lambda: map(int, input().split())

t = gi()

for _ in range(t):
    n, k, m = gmi()
    
    if k > m:
        print("NO")
    else:
        print("YES")
        ans = []
        val = m - k + 1
        for i in range(1, n + 1):
            if i % k == 0:
                ans.append(val)
            else:
                ans.append(1)
        print(*ans)