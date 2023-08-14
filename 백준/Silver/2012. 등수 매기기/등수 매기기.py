import sys

n = int(input())
m = 0
data = [int(sys.stdin.readline()) for _ in range(n)]
data.sort()

for i in range(n):
  m += abs(data[i] - (i+1))

print(m)