import sys

n = int(sys.stdin.readline())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: x[0])
arr.sort(key=lambda x: x[1])
end = 0
cnt = 0

for i, j in arr:
  if end <= i:
    end = j
    cnt += 1

print(cnt)
