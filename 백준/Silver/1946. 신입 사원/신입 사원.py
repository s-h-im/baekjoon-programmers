import sys

t = int(sys.stdin.readline().strip())
new = [1 for _ in range(t)]
for j in range(t):
    n = int(sys.stdin.readline().strip())
    workers = [[int(x) for x in sys.stdin.readline().split()] for _ in range(n)]
    workers.sort()
    min_rank = workers[0][1]
    for i in range(n):
        rank = workers[i][1]
        if rank < min_rank:
            min_rank = rank
            new[j] += 1

for i in range(t):
  print(new[i])