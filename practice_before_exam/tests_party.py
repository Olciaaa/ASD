import time 

TEST_SPEC = [
# N (maksymalna głębokość), k (max. liczba dzieci), w (max. wartość), hint (poprawna odpowiedź)
  (3, 3, 20, 60),
  (3, 4, 100, 264),
  (5, 5, 100, 6041),
  (10, 5, 1000, 223226),
  (10, 7, 1000, 23877934),
  (5, 20, 100, 5163763),
  (5, 25, 100, 10455131),
  (6, 15, 100, 3826133),
  (6, 18, 100, 23828576),
  (6, 20, 100, 56897880)
]

MY_seed    = 25
MY_a       = 134775813
MY_c       = 1
MY_modulus = 2**32

def MY_random():
   global MY_seed, MY_a, MY_c, MY_modulus
   MY_seed = (MY_a * MY_seed + MY_c) % MY_modulus
   return MY_seed

class Employee:
    def __init__(self, fun):
        self.fun = fun 
        self.emp = []
        self.f = -1 
        self.g = -1

def generateEmployees(head, n, maxn, maxk, maxw):
    if n > maxn:
        return 

    count = MY_random()%maxk 
    if n <= 2 and count == 0:
        count = 1
    for i in range(count):
        empC = Employee(MY_random()%maxw)
        head.emp.append(empC)
        generateEmployees(empC, n+1, maxn, maxk, maxw)

def runtests( f ):
    total = 0 
    zaliczone = 0 
    testy = 0
    i = 0
    
    for el in TEST_SPEC:
        root = Employee(MY_random()%el[2])
        generateEmployees(root, 1, el[0], el[1], el[2])
        
        start = time.time()
        sol = f(root)
        end = time.time()
        total += (end-start)
        testy += 1 
        if sol == el[3]:
            print("TEST #", i, " zaliczony")
            print("Twoja odpowiedz: ", sol, "\nPoprawna odpowiedz: ", el[3])
            print("Czas trwania: %.2f sek.\n" %float(end-start))
            zaliczone += 1
        else:
            print("TEST #", i, " NIEZALICZONY!")
            print("Twoja odpowiedz: ", sol, "\nPoprawna odpowiedz: ", el[3])
            print("Czas trwania: %.2f sek.\n" %float(end-start))

        i += 1
    print("Zaliczone testy: ", zaliczone, "/", testy)
    print("Orientacyjny łączny czas: %.2f sek." %float(total))

