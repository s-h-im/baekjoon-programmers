n, m = map(int, input().split()) 

arr = []
for i in range(n):
  arr.append(input())

dna = '' 
for j in range(m):
  dic = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
  for i in range(n):
    acgt = arr[i][j]
    dic[acgt] += 1
  dna += max(dic, key=dic.get) 

hd = 0
for i in range(n):
  for j in range(m):
    if dna[j] != arr[i][j]:
      hd += 1

print(dna)
print(hd)