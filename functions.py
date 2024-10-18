def get_unique_list_f(lst):
       return list(set(lst))

def count_case_f(string):
    uppercase_qty = sum(1 for letter in string if letter.isupper())
    lowercase_qty = sum(1 for letter in string if letter.islower())
    return (uppercase_qty,lowercase_qty)

import re
def word_count_f(sentence):
    cleaned_sentence = re.sub(r'[^\w\s]','',sentence)
    words = cleaned_sentence.split()
    return len(words)

def add_fab(a,b):
    return a+b

def subtract_f(a,b):
    return a-b

def multiply_f(a,b):
    return a*b

def divide_f(a,b):
    if b ==0:
        return "Error"
    return a/b

def calculate_f(a,b,operator):
    if operator =='+':
        return add(a,b)
    elif operator =='-':
        return subtract(a,b)
    elif operator =='*':
        return multiply(a,b)
    elif operator =='/':
        return divide(a,b)
    else:
        return "Error"

def add_f(*args):
    result = 0
    for num in args:
        result += num
    return result

def subtract_f(*args):
    result = args[0]
    for num in args[1:]:
        result -= num
    return result

def multiply_f(*args):
    result = 1
    for num in args:
        result *= num
    return result
    
def divide_f(*args):
    result = args[0]
    try:
        for num in args[1:]:
            result /= num
    except ZeroDivisionError:
        return "Error: Division by zero."
    return result

def calculate_f(operator, *args):
    if operator == '+':
        return add(*args)
    elif operator == '-':
        return subtract(*args)
    elif operator == '*':
        return multiply(*args)
    elif operator == '/':
        return divide(*args)
    else:
        return "Error: invalid operator."