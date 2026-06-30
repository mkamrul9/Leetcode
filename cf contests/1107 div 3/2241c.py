import sys

# sys.stdout = open('output.txt', 'w')
# sys.stdin = open('input.txt', 'r')

input = lambda: sys.stdin.readline().strip()
gi = lambda: int(input())
gs = lambda: input().split()

t = gi()

for i in range(t):
    n = int(input())
    s = input()
    
    has_10 = "10" in s
    has_01 = "01" in s
 
    if not has_10 and not has_01:
        minwf = 1
    elif has_10 and has_01:
        minwf = 1

    else:
        minwf = 2
        
    print(minwf)
    