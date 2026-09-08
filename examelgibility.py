medical=input(" do you have a medical cause? (Y/N): ")
if medical=="Y":
        print("student is allowed to take the exam.")
else:
        attendance=int(input("enter your attendance percentage: "))
        if attendance>=75:
                print("student is allowed to take the exam.")
        else:
                print("the student is not allowed to take the exam.")