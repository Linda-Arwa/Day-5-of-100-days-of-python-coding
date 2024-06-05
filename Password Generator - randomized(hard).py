# This program is a password generator

#Password Generator Project

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# We shall have a list of our passwords called password_list

password_list = []

# For letters password
for char in range(1, nr_letters+1):
    password_list.append(random.choice(letters)) # append() adds to a list
    
# For numbers password
for char in range(1, nr_numbers+1):
    password_list.append(random.choice(numbers))
    
# For symbols password
for char in range(1, nr_symbols+1):
    password_list.append(random.choice(symbols))
    
# print(password_list)

# We have to shuffle the items in the list using the shuffle()
random.shuffle(password_list)
# print(password_list)

# We now have convert the list to a string
password = ""

for char in password_list:
    password = password + char
    
print(f"Your password is: {password}")
