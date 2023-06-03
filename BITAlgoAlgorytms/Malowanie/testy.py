# testy.py
# from signal import signal, alarm, SIGALRM
import sys
# To należy ustawić
TAB = [6, 11, 16]
###################
TIMER = False
RERAISE = True
if TIMER:
  from signal import signal, alarm, SIGALRM

from copy import deepcopy
import time

def limit( L, lim=120 ):
  x = str( L )
  if len(x) < lim:
    return x
  else:
    return x[:lim]+"[za dlugie]..."

def print_err(*a):
     print(*a, file = sys.stderr)

class TimeOut(Exception):
  def __init__(self):
    pass
     
def timeout_handler( signum, frame ):
   raise TimeOut()

def internal_runtests( copyarg, check, TESTS, f, ACC_TIME, all_tests ):
  passed = 0
  total  = len(TESTS)
  total_time = 0
  erros_set = None
  for i,d in enumerate(TESTS):
    if i >= TAB[all_tests]:
      break
    print("--------------------------------------")
    print("Test", i )
    arg  = copyarg(d["arg"])
    arg2 = copyarg(d["arg"])
    hint = deepcopy(d["hint"])
    try:
      if TIMER:
        signal( SIGALRM, timeout_handler )
        alarm( ACC_TIME + 1)
      time_s = time.time()
      end    = time.time() 
      sol    = f( *arg )
      time_e = time.time()
      
      if TIMER:
        alarm(0)
      res = check( *arg2, hint, sol )
      if ACC_TIME > 0 and float(time_e-time_s) > ACC_TIME:
        print("!!!!!!!! PRZEKROCZONY DOPUSZCZALNY CZAS")
      elif res:
        passed += 1
        print("Test zaliczony!")
      else:
        print("TEST NIEZALICZONY!!!")
        # To zmienić
        if erros_set:
          erros_set.append(f"mal{'{:0>2}'.format(str(i))}")
        else:
          erros_set = [f"mal{'{:0>2}'.format(str(i))}"]
      print("Orientacyjny czas: %.2f sek." % float(time_e-time_s))
        
      total_time += float(time_e-time_s)
    except TimeOut:
      print("!!!!!!!! PRZEKROCZONY DOPUSZCZALNY CZAS")
    except KeyboardInterrupt:
      print("Obliczenia przerwane przez operatora")
    except Exception as e:
      print("WYJATEK:", e)
      if RERAISE: raise e
    
    
  print("--------------------------------------")
  print("Liczba zaliczonych testów  : %d/%d" % (passed,min(total, TAB[all_tests])) )
  print(f"Lista niezaliczonych testów: {limit(erros_set)}")
  print("Orientacyjny łączny czas   : %.2f sek." % total_time )

  print_err(sys.argv[0].replace("_"," ").replace(".py",""), passed, min(total, TAB[all_tests]), "%.2f" % total_time)
