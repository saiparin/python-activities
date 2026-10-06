print("the pyramid pattern is(*):")
n=int(input("enter the amount of rows:"))
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()