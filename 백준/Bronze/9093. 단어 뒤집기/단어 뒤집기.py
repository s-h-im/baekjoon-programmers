t = int(input())
a = []
for _ in range(t):
  b = input().split()
  a.append(b)

for k in range(t):
  for i in a[k]:
    for j in range(len(i)):
      print(i[abs(len(i) - j) - 1], end="")
    print(" ", end="")
  print()