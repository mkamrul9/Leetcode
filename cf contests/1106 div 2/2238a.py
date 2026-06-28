import sys

# sys.stdout = open('output.txt', 'w')
# sys.stdin = open('input.txt', 'r')

input = lambda: sys.stdin.readline().strip()
gi = lambda: list(map(int, input().split()))
gs = lambda: input().split()

t = int(input())

for i in range(t):
    n, c = gi()
    a = gi()
    b = gi()
    
    sum_a = sum(a)
    sum_b = sum(b)

    check = True
    for j in range(n):
        if a[j] < b[j]:
            check = False
            break
            
    if check:
        print(sum_a - sum_b)
        continue

    a.sort()
    b.sort()
    
    check_with = True
    for j in range(n):
        if a[j] < b[j]:
            check_with = False
            break
            
    if check_with:
        print(sum_a - sum_b + c)
    else:
        print(-1)