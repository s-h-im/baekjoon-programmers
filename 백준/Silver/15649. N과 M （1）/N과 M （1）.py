import sys
n, m = map(int, sys.stdin.readline().split(' '))

arr = [0 for _ in range(m)]
remain = [for _ in range(m)]
def dfs(cnt):
	if cnt = m:
		print(' '.join(map(str, arr)))
		return
	for i in range(1, n + 1):
		arr[cnt] = i
		dfs(cnt + 1)

dfs(0)
