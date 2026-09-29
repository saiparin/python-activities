number= int(input("enter a starting range: "))
upper= int(input("enter the max limit:"))
print("the prime number between",number,"and",upper,"are:")
for num in range(number,upper+1):
    if num > 1:
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            print(num)    