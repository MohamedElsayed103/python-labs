def guess():
    import random
    number_to_guess = random.randint(1, 20)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 and 20: "))
            attempts += 1

            if guess < 1 or guess > 20:
                print("Please guess a number within the range of 1 to 20.")
                continue

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")



def cart():
    cart = {}
    while True:
        print("1. Add item")
        print("2. Remove item")
        print("3. View cart")
        print("4. Checkout and exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            name = input("Enter item name: ").strip()
            if not name:
                print("Item name cannot be empty.")
                continue
            try:
                price = float(input("Enter item price: "))
                if price < 0:
                    print("Price cannot be negative.")
                    continue
            except ValueError:
                print("Invalid price. Please enter a valid price value.")
                continue
            cart[name] = price
            print(f"Added {name} with price {price} to the cart.")

        elif choice == "2":
            name = input("Enter item name to remove: ").strip()
            if name in cart:
                del cart[name]
                print(f"Removed {name} from the cart.")
            else:
                print(f"{name} not found in the cart.")

        elif choice == "3":
            if not cart:
                print("Your cart is empty.")
            else:
                print("Items in your cart:")
                for item, price in cart.items():
                    print(f"{item}: ${price}")
                total = sum(cart.values())
                print(f"Total cost: ${total}")

        elif choice == "4":
            total = sum(cart.values())
            print(f"Checking out. Total cost: ${total}")
            break

        else:
            print("Invalid choice. Please select a valid option.")



def gradeBook():
    students = {}
    while True:
        for _ in range(5):
            while True:
                name = input("Enter student name: ").strip().lower()
                if not name:
                    print("Name cannot be empty. Please try again.")
                    continue
                if name in students:
                    print("This name has already been entered. Please enter a different name.")
                    continue
                if not name.isalpha():
                    print("Name must contain only alphabetic characters. Please try again.")
                    continue
                break

            while True:
                try:
                    score = float(input(f"Enter score for {name}: "))
                    if score < 0 or score > 100:
                        print("Score must be between 0 and 100. Please try again.")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please enter a numeric score.")

            students[name] = score

        if students:
            scores = students.values()
            print(f"Highest score: {max(scores)}")
            print(f"Lowest score: {min(scores)}")
            print(f"Average score: {sum(scores) / len(scores)}")
        else:
            print("No students entered.")
        break


def countWords():
    while True:
        sentence = input("Enter a sentence: ").strip()
        if not sentence:
            print("Input cannot be empty. Please enter a valid sentence.\n")
            continue
        words = sentence.split()
        word_count = {}
        for word in words:
            if not word.isalpha():
                continue
            word = word.lower()  
            word_count[word] = word_count.get(word, 0) + 1
        print("Word counts:")
        for word, count in word_count.items():
            print(f"{word=}: {count=}")
        break








def removeDuplicatesSortDisplay():
    while True:  
        raw = input("Enter List of numbers : ")
        elements = raw.split()
        try:
            numbers = {int(x) for x in elements} 
        except ValueError:
            print("Invalid input. Please enter only numbers.\n")
            continue
        print("Sorted numbers:", sorted(numbers))
        break








def sortFiveNumbers():
    while True:  

        raw = input("Enter exactly 5 numbers : ")
        elements = raw.split()

        if len(elements) > 5:
            print("You entered more than 5 numbers . Please enter five numbers.\n")
            continue  
        if len(elements) < 5:
            print("You entered less than 5 numbers . Please enter five numbers.\n")
            continue  
        try:
            numbers = [int(x) for x in elements] 
        except ValueError:
            print("Invalid input. Please enter only numbers.\n")
            continue
        print("Sorted numbers:", sorted(numbers))
        print("Sorted numbers reversed :", sorted(numbers, reverse=True))
        break  


def show():
    nums=[]
    sums=0
    count=0
    while True:
        num=input("Enter a number or done to show the results: ")
        if num.lower() == "done":
            print("Total:", sums)
            print("Count:", count)
            if count > 0:
                print("Average:", sums / count)
            else:
                print("No valid numbers entered.")
            break
        try:
            number = float(num)
            nums.append(number)
            sums += number
            count += 1
        except ValueError:
            print("Invalid input. Please enter a number or 'done' to finish.")



def seq():
    while True:
        try:
            length = int(input("Enter the length of the sequence (positive integer): "))
            start = int(input("Enter the starting number (integer): "))
            if length <= 0:
                print("Length must be a positive integer. Please try again.\n")
                continue
            sequence = [start + i for i in range(length)]
            print("Sequence:", sequence)
            break  
        except ValueError:
            print("Invalid input. Please enter valid integers.\n")


def mainMenu():
    while True:
        print("=== The System ===")
        print("1. Sort five numbers")
        print("2. print sequence of numbers starting from a given number")
        print("3. Calculate total, count, and average of valid entered numbers")
        print("4. Remove duplicates, sort, and display numbers")
        print("5. Count word occurrences in a sentence")
        print("6. Gradebook system")
        print("7. Shopping cart system")
        print("8. Number guessing game")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            sortFiveNumbers()
        elif choice == "2":
            seq()
        elif choice == "3":
            show()
        elif choice == "4":
            removeDuplicatesSortDisplay()
        elif choice == "5":
            countWords()
        elif choice == "6":
            gradeBook()  
        elif choice == "7":
            cart()
        elif choice == "8":
            guess()
        else:
            print("Invalid choice, please try again.\n")


mainMenu()