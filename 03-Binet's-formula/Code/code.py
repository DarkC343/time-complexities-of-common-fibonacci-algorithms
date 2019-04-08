# Coded by DarkC343
# 972
from timeit import default_timer as timer
import csv
import sys
from math import floor, sqrt
from decimal import *

def fib(n):
    phi = (1 + 5**.5) / 2
    psi = (1 - 5**.5) / 2
    return Decimal((phi**n - psi**n) / 5**.5)

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
