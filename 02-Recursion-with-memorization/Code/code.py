# Coded by DarkC343
# 972
from timeit import default_timer as timer
import csv
import sys

def fib2_recur(n, F):
    if F[n] == None:
        if n == 0:
            F[n] = 0
        elif n == 1:
            F[n] = 1
        else:
            F[n] = fib2_recur(n - 1, F) + fib2_recur(n - 2, F)
    return F[n]

def fib(n):
    r = fib2_recur(n, [None] * (n + 1))
    return r

sys.setrecursionlimit(1505)

with open('results.csv', mode='w') as results_file:
    results_writer = csv.writer(results_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    results_writer.writerow(['n', 'elapsed', 'output'])
    for number in range(1500):
        start = timer()
        output = fib(number)
        end = timer()
        results_writer.writerow([number, end - start, output])
        print(str(number) + ": done")
