import sys

x = int(sys.stdin.readline())
line = 1

while x > line:
  x -= line
  line += 1

if line%2==0:
  print(x, "/", line+1-x, sep='')
else:
  print(line+1-x, "/", x, sep='')