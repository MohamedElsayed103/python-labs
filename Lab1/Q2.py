
#- application to take a number in binary form from the user, and print it as a decimal

binary = input("Enter a binary number: ").strip()
isBinary = True
for ch in binary:
    if ch not in "01":
        isBinary = False
        break

if binary != "" and isBinary:
    decimal = int(binary, 2)
    print(f"The decimal value is {decimal}")
else:
    print("Invalid input enter 0s and 1s.")
