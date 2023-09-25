import sys

n = int(sys.stdin.readline())
s = [] 
p = [] 

for _ in range(n):
  a = sys.stdin.readline().split() 
  if a[0] == "push":
    s.append(a[1]) 
  elif a[0] == "pop":
    if len(s) > 0:
      p.append(s[len(s)-1])
      s.pop()
    else:
      p.append(-1)
  elif a[0] == "size":
   p.append(len(s))
  elif a[0] == "empty":
    if len(s) > 0:
      p.append(0)
    else:
      p.append(1)
  elif a[0] == "top":
    if len(s) > 0:
      p.append(s[len(s) - 1])
    else:
      p.append(-1)
      
for i in p:
  print(i)