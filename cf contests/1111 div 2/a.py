import sys

# sys.stdout = open('output.txt', 'w')
# sys.stdin = open('input.txt', 'r')

input = lambda: sys.stdin.readline().strip()
gi = lambda: int(input())
gmi = lambda: map(int, input().split())

t = gi()

for _ in range(t):
    n = gi()
    a = list(gmi())
    
    if n % 2 != 0:
        print("NO")
    else:
        count_minus_1 = a.count(-1)
        target = n // 2
        
        if count_minus_1 % 2 == target % 2:
            print("YES")
        else:
            print("NO")