name=input("enter the word:")
answer=input("enter the letter:")
i=0
count=0
while(i<len(name)):
    if(name[i]==answer):
        count=count+1
    i=i+1 
print("the letter is used",count,"times")