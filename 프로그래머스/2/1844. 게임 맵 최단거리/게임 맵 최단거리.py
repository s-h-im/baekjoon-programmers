from collections import deque

def bfs(maps, x, y):
    answer = 0
    q = deque()
    q.append((x, y))
    n = len(maps)
    m = len(maps[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if maps[nx][ny] == 0:
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx, ny))
    return maps[n - 1][m - 1]


def solution(maps):
    answer = bfs(maps, 0, 0)
    if answer == 1:
        answer = -1
    return answer
