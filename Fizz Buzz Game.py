# This is the Fizz Buzz Game
# Instructions:
# The program should print numbers 1 to 100
# If a number is divisible by 3, print Fizz, if divisile by 5, print Buzz but incase the number is divisible by both 3 and 5, print FizzBuzz

# Solution

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
        
    elif number % 3 == 0:
        print("Fizz")
        
    elif number % 5 == 0:
        print("Buzz")
        
    else:
        print(number)
        