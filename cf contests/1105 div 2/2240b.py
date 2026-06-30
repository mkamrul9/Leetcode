import sys

sys.stdout = open('output.txt', 'w')


input = lambda: sys.stdin.readline().strip()
gi = lambda: list(map(int, input().split()))
gs = lambda: input().split()

t = int(input())
