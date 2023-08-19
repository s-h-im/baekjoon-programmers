from collections import deque

def bfs(v):
  q = deque([v]) 
  v1[v] = 1 
  while q:  
    front = q.popleft() 
    print(front, end=" ") 
    for i in range(1, n + 1):
      if v1[i] == 0 and g[front][i] == 1:
        q.append(i)  
        v1[i] = 1 

def dfs(v):
  v2[v] = 1  
  print(v, end=' ')
  for i in range(1, n + 1):
    if v2[i] == 0 and g[v][i] == 1:
      dfs(i)


n, m, v = map(int, input().split())
g = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
v1 = [0] * (n + 1) 
v2 = [0] * (n + 1)

for i in range(m):
  a, b = map(int, input().split())
  g[a][b] = g[b][a] = 1

dfs(v)
print()
bfs(v)