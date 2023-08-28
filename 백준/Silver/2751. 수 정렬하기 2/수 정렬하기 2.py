import sys

n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n)]
sorted_arr = sorted(arr)
for i in sorted_arr:
  print(i)