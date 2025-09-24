
# Lab:
# 	- write a program that prints hello world

# print("Hello World")

# 	- application to take a number in binary form from the user, and print it as a decimal

# binary = input("Enter a binary number: ").strip()

# isBinary = True
# for ch in binary:
#     if ch not in "01":
#         isBinary = False
#         break

# if binary != "" and isBinary:
#     decimal = int(binary, 2)
#     print(f"The decimal value is {decimal}")
# else:
#     print("Invalid input enter 0s and 1s.")

# 	- write a function that takes a number as an argument and if the number
# 		divisible by 3 return "Fizz" and if it is divisible by 5 return "buzz" and if is is
# 		divisible by both return "FizzBuzz"

# def fizz(num):
#     if num % 3 == 0 and num % 5 == 0:
#         return "FizzBuzz"
#     elif num % 3 == 0:
#         return "Fizz"
#     elif num % 5 == 0:
#         return "Buzz"
#     else:
#         return "Not Fizz Or Buzz"

# print(fizz(15))
# print(fizz(5))
# print(fizz(3))

# 	- Ask the user to enter the radius of a circle print its calculated area and circumference

# pi = 3.14
# radius = float(input("\nEnter the radius: "))
# area = pi * radius ** 2
# circumference = 2 * pi * radius
# print(f"Area: {area}")
# print(f"Circumference: {circumference}")

# 	- Ask the user for his name then confirm that he has entered his name (not an empty string/integers).
# 	 then proceed to ask him for his email and print all this data

# name = input("\nEnter your name: ").strip()
# while not name.isalpha():
#     print("Invalid name")
#     name = input("Enter your name: ").strip()

# email = input("Enter your email: ").strip()
# while "@" not in email or "." not in email :
#     print("Invalid email")
#     email = input("Enter your email: ").strip()
# print(f"Name: {name}, Email: {email}")  

# 	- Write a program that prints the number of times the substring 'iti' occurs in a string

# text = input("Enter a string: ")
# count = text.count("iti")
# print(count)