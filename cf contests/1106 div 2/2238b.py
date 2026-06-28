import sys

sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

input = lambda: sys.stdin.readline().strip()
gi = lambda: list(map(int, input().split()))
gs = lambda: input().split()

t = int(input())

for i in range(t):
    n = int(input())

    triples = 0
    
    for i in range(1, n + 1):
        multiples = n // i
        triples += multiples * multiples
        
    print(triples)