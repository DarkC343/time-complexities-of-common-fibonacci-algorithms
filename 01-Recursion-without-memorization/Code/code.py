# Coded by DarkC343
# 972
from timeit import default_timer as timer
import csv

def fib(n):
    if n == 1: return 1
    elif n == 0: return 0
    else: return fib(n - 1) + fib(n - 2)

with open('results.csv', mode='w') as results_file:
    results_writer = csv.writer(results_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    results_writer.writerow(['n', 'elapsed', 'output'])
    for number in range(50):
        start = timer()
        output = fib(number)
        end = timer()
        results_writer.writerow([number, end - start, output])
        print(str(number) + ": done")
