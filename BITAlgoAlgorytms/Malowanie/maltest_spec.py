import os
ALLOWED_TIME = 1000
# To należy ustawić ręcznie
TEST_NUM = 16

# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

# To należy napisać zależnie od zadania
def make_test(i):
    path = os.path.dirname(os.path.abspath(__file__))
    file_in     = open(f"{path}\\TEST_DIR\\mal{'{:0>2}'.format(str(i))}.in", "r")
    file_out    = open(f"{path}\\TEST_DIR\\mal{'{:0>2}'.format(str(i))}.out", "r")

    # Tutaj należy napisać czytanie plików
    temp = file_in.readline().rsplit(" ")
    temp[-1] = temp[-1][:-1]
    n, k, p = int(temp[0]), int(temp[1]), int(temp[2])

    output = int(file_out.readline())

    return (n, k, p, output)

TEST_SPEC = [make_test(i) for i in range(TEST_NUM)] 