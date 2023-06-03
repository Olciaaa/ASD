'''
Proszę zaimplementować rozwiązanie problemu “Impreza firmowa” tak, by zwracane były imiona pracowników, którzy idą na imprezę.
Znaleźć wartość najlepszej dopuszczalnej imprezy. Dopuszczalna jest jeżeli nie zaprosiliśmy bezpośredniego przełożonego żadnego
pracownika. Wartość jest oceniana jako dodana wartość fun kazdego pracownika na imprezie
emp to podwładni
fun to wartość imprezy
'''
from tests_party import runtests
class Employee:
    def __init__(self, fun):
        self.fun = fun
        self.emp = []
        self.f = -1
        self.g = -1

def could_be_going(employee):
    if employee.f != -1: return employee.f

    value = employee.fun
    for el in employee.emp:
        value += not_going(el)
    employee.f = max(value, not_going(employee))
    return employee.f

def not_going(employee):
    if employee.g != -1: return employee.g

    employee.g = 0

    for el in employee.emp:
        employee.g += could_be_going(el)
    return employee.g

def party(root):
    return could_be_going(root)

runtests ( party )