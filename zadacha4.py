# Составить список из элементов последовательности факториала числа

def find_factorial(n):
    factorial = 1
    list_factorial = []
    for i in range (1,n+1):
        factorial *= i
        list_factorial.append(factorial)
    print(list_factorial)

find_factorial(4)