import sys

sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

input = lambda: sys.stdin.readline().strip()
gi = lambda: int(input())
gmi = lambda: map(int, input().split())

t = gi()

for _ in range(t):
    n, c = gmi()
    a = list(gmi())
    
    a = a[::-1]
    
    
    s_base = sum(a) - n * c
    

    p = [c - x for x in a]
    

    p.sort(reverse=True)
    
    ans = s_base
    limit = n // 2
    

    for i in range(limit):
        if p[i] > 0:
            ans += p[i]
        else:
            break
            
    print(ans)