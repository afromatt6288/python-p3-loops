#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i=10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")
    pass

def square_integers(int_list):
    # code goes here!
    # squared_integers = list()
    # for integer in int_list:
    #     squared_int = integer * integer
    #     squared_integers.append(squared_int)
    #     return squared_integers
    squared_integers=[integer * integer for integer in int_list]
    return squared_integers
    pass

def fizzbuzz():
    for i in range(1, 101):
        if i == 0:
            None
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
    pass
    # code goes here!
