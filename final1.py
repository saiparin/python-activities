try:
    num1,num2=eval(input("enter two numbers,separated by a comma: "))
    result  =num1/num2
    print("the Result is",result)
except ZeroDivisionError:
    print("the Division by zero is error")
except SyntaxError:
    print("Comma is missing in between the two numbers")
except:
     print("wrong input")
else:
    print("NO exceptions")
finally:
    print("the program is working fine")
