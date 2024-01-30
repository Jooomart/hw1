from math import *
num = int(input('Число:'))
num_buket = 1
for num_iter in range(1, num+1):
    num_buket *= num_iter
print(num_buket)

factor = factorial(int(input('Число:')))
print(factor)
