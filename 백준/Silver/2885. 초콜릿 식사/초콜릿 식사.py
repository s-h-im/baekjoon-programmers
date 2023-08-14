import sys

k = int(sys.stdin.readline())
cnt = 0

n = 1
while n < k:
  n <<= 1

n1 = n #n 기록용

while k > 0:
  if k >= n:
    k -= n
  else:
    n //= 2
    cnt += 1

print(n1, cnt)