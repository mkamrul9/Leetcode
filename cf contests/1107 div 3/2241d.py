import sys

sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

input = lambda: sys.stdin.readline().strip()
gi = lambda: int(input())

t = gi()

for _ in range(t):
    n = gi()
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    
    e = [0] * (n + 2)
    for i in range(1, n + 1):
        diff = b[i-1] - a[i-1]
        if i % 2 == 1:
            e[i] = diff
        else:
            e[i] = -diff
            
    iswf = True
    sum_odd = 0
    sum_even = 0
    
    for i in range(1, n + 2):
        d_i = e[i] - e[i-1]
        if i % 2 == 1:
            sum_odd += d_i
        else:
            sum_even += d_i
            
        if sum_odd < 0 or sum_even > 0:
            iswf = False
            break
            
    print("YES" if iswf else "NO")