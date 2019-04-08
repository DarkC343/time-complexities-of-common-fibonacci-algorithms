# Coded by DarkC343
# 972
from timeit import default_timer as timer
import csv

def fib(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a

with open('results.csv', mode='w') as results_file:
    results_writer = csv.writer(results_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    results_writer.writerow(['n', 'elapsed', 'output'])
    for number in range(10000):
        start = timer()
        output = fib(number)
        end = timer()
        results_writer.writerow([number, end - start, output])
        print(str(number) + ": done")
