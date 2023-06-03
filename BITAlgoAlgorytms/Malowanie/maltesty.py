# zad1testy.py
from testy import *
from maltest_spec import ALLOWED_TIME, TEST_SPEC

def copyarg( arg ):
    return arg

# To należy ustawić do zadania
def check(n, k, p, hint, sol):
    return hint == sol

# To należy ustawić do zadania
def gentest(n, k, p, output):
    return (n, k, p), output

def runtests( f, all_tests = 1 ):
    TESTS = []
    for spec in TEST_SPEC:
        newtest = {}
        arg, hint = gentest(*spec)
        newtest["arg"] = arg
        newtest["hint"] = hint
        TESTS.append(newtest)

    internal_runtests(copyarg, check, TESTS, f, ALLOWED_TIME, all_tests)

