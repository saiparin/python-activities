amount=int(input("enter the amount"))

bill_1= amount//200
bill_2= (amount%200)//100
bill_3= (amount%200%100)//50

print("the number of 200 bill is", bill_1)
print("the number of 100 bill is", bill_2)
print("the number of 50 bill is", bill_3)