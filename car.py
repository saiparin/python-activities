print("Select your ride: ")
print("1. Bike")
print("2. Car")

#select your ride
choice = int( input("Enter your choice: ") )

#User entering option 1 
if( choice == 1 ): 
  print( "what type of bike? " )
  print("1.Scooty\n")
  print("2.Scooter\n")

  #Condition for selecting the type of bike
  choice2=int(input("Enter you choice2: "))
  if choice2==1:
    print("you have selected scooty")
  else:
    print("you have selected scooter")

#User entering option 2
elif( choice == 2 ): 
  print( "what type of car?" )
  print("1.Sedan")
  print("2.XUV")
  choice3=int(input("enter your choice3: "))

  if choice3==1: 
  #condition for selecting the type of car
    print("you have selected sedan")
  else:
    print("you have selected XUV")

else: 
  print("Wrong choice!")