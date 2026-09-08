Units=int(input("enter the number of units consumed: "))
if (Units<=50):
    bill=Units*2.60
    print("the bill amount is: ", bill)
if(Units>50 and Units<=100):
    bill=130+Units*3.25
    print("the bill amount is: ", bill)  
if(Units>100 and Units<=200):
    bill=130+162.50+Units*5.26
    print("the bill amount is: ", bill)
if(Units>200):
    bill=130+162.50+526+Units*7.87
    print("the bill amount is: ", bill)