from egzP3atesty import runtests
from math import inf

class Node:
  def __init__(self, wyborcy, koszt, fundusze):
    self.next = None
    self.wyborcy = wyborcy 
    self.koszt = koszt
    self.fundusze = fundusze 
    self.x = None

def rec(el, leftMoney):
    if el is None:
        return 0

    if el.x[leftMoney] != -1:
        return el.x[leftMoney]

    if leftMoney - el.koszt < 0:
        el.x[leftMoney] = rec(el.next, leftMoney)
        return rec(el.next, leftMoney)

    el.x[leftMoney] = max(rec(el.next, leftMoney - el.koszt) + el.wyborcy, rec(el.next, leftMoney))
    return max(rec(el.next, leftMoney - el.koszt) + el.wyborcy, rec(el.next, leftMoney))

def wybory(T):
    toReturn = 0

    for el in T:
        current = el
        while current is not None:
            current.x = [-1 for _ in range(current.fundusze + 1)]
            current = current.next

    for el in T:
        toReturn += max(rec(el.next, el.fundusze - el.koszt) + el.wyborcy, rec(el.next, el.fundusze))

    return toReturn

runtests(wybory, all_tests = True)