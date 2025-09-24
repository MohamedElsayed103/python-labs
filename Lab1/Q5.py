
# 	- Ask the user for his name then confirm that he has entered his name (not an empty string/integers).
# 	 then proceed to ask him for his email and print all this data

name = input("\nEnter your name: ").strip()
while not name.isalpha():
    print("Invalid name")
    name = input("Enter your name: ").strip()

email = input("Enter your email: ").strip()
while "@" not in email or "." not in email :
    print("Invalid email")
    email = input("Enter your email: ").strip()
print(f"Name: {name}, Email: {email}")  
