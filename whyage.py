user_input = input("Enter your age: ")

try:
    age = int(user_input)
    if age % 2 == 0:
        print("Your age is even.")
    else:
        print("Your age is odd.")
except ValueError:
    print("Error: Please enter a valid whole number.")