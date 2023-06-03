from math import inf
from zad3testy import runtests

Data = []
dynamic = []

def kintersect( A, k ):
  """Miejsce na Twoją implementację"""
  global Data, dynamic
  Data = A
  dynamic = [[-1 for _ in range(len(Data) + 1)]for _ in range(k + 1)]

  for i in range(len(Data)):
    Data[i] = (Data[i][0], Data[i][1], i)
  Data.sort(key = lambda x: (x[0], x[1]))
  #print(Data)
  a, b = rec(0, k)
  print(b - a)

  #for el in dynamic:
    #print(el)

  return []

def rec(idx, left_k):
  global Data, dynamic

  if left_k == 0:
    dynamic[left_k][idx] = (0, inf)
    return (0, inf)

  if idx == len(Data) or len(Data) - idx < left_k:
    dynamic[left_k][idx] = (inf, 0)
    return (inf, 0)

  if dynamic[left_k][idx] != -1:
    return dynamic[left_k][idx]

  start1, end1 = rec(idx + 1, left_k - 1)
  start1 = max(start1, Data[idx][0])
  end1 = min(end1, Data[idx][1])

  start2, end2 = rec(idx + 1, left_k)

  start = start1
  end = end1

  if end2 - start2 > end - start:
    start = start2
    end = end2

  dynamic[left_k][idx] = (start, end)
  return (start, end)

A = [(0,4),(1,10),(6,7), (2,8)]
k = 3
#print(kintersect(A, k))
runtests( kintersect )