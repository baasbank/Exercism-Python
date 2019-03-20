# Initial solution

from math import pow

def is_armstrong(number):
    number_list = list(str(number))
    calculate_armstrong = 0
    for i in number_list:
        calculate_armstrong += pow(int(i), len(number_list))
    if calculate_armstrong == number:
        return True
    return False

# Better still (or should I say shorter still? :))

def is_armstrong(number):
    return sum([int(i) ** len(str(number)) for i in str(number)]) == number


