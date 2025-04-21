import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# Taking a input from user
in_letters=int(input("How many letter do you want "))
in_numbers=int(input("How many numbers do you want "))
in_symbols = int(input("How many symbols do you want "))
password_list = []
for char in range(0,in_letters):
    password_list.append(random.choice(letters))
for char in range(0,in_numbers):
    password_list.append(random.choice(numbers))
for char in range(0,in_symbols):
    password_list.append(random.choice(symbols))

print(password_list)
random.shuffle(password_list)
# Adding it to the string 
password = ""
for i in password_list:
    password += i

print(password)

