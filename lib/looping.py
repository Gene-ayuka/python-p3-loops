#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    count = 10
    while count > 0:
        print(count)
        count -= 1
    print("Happy New Year!")

# Example usage:
# happy_new_year()

    pass

def square_integers(integers):
    # code goes here!
    
    return [num ** 2 for num in integers]

# Example usage:
# squared_numbers = square_integers([1, 2, 3, 4])
# print(squared_numbers)  # Output: [1, 4, 9, 16]

    pass

def fizzbuzz():
    # code goes here!
    for num in range(1, 101):  # Loop from 1 to 100 (inclusive)
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

    pass