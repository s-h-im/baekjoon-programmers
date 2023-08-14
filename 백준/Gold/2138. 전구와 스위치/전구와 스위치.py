n = int(input())
before1 = list(map(int, input()))
before2 = before1[:] 
after = list(map(int, input()))
cnt = 0

for i in range(1, n):
  if before1[i - 1] != after[i - 1]:
    cnt += 1 
    before1[i - 1] = int(not before1[i - 1])
    before1[i] = int(not before1[i]) 
    if i != n - 1:
      before1[i + 1] = int(not before1[i + 1])
else:
  if ''.join(map(str, before1)) == ''.join(map(str, after)):
    print(cnt)
    exit()

cnt = 1
before2[0] = not before2[0]
before2[1] = not before2[1]
for i in range(1, n):
  if before2[i - 1] != after[i - 1]:
    cnt += 1
    before2[i - 1] = int(not before2[i - 1])
    before2[i] = int(not before2[i])  
    if i != n - 1:
      before2[i + 1] = int(not before2[i + 1])
else:
  if ''.join(map(str, before2)) == ''.join(map(str, after)):
    print(cnt)
    exit()

print(-1)
