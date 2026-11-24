print("calculator")
print("1.ADDITION(+)")
print("2.SUBTRACTION(-)")
print("3.MULTIPLICATION(*)")
print ("4.DIVISION(/)")
try:
    choice =input("choose an operation from 1,2,3,4:")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1": 
       result= add(num1,num2)
       print("Result:",result)

    elif choice == "2":
        result= subtract(num1,num2)
        print("Result:",result)
    elif choice == "3":
        result= multiply(num1, num2)
        print("Result:",result)

    elif choice == "4":
        result= divide(num1,num2)
        print("Result:",result)
        
    else:
            print("Error: please enter valid numbers.")

    
       
except ValueError:
    print("Invalid input. Please enter valid numbers.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")