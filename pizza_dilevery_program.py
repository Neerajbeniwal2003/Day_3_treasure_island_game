print("welcome to python pizza deliveries:)")
size=input("what size do you want? S ,M or L:")
pepparoni=input("do you want pepperoni for pizza? y or n:")
e_cheese=input("do you want extra cheese? y or n:")
bill=0
if size=="s":
    bill=15
    if pepparoni=="y":
        bill+=2
    if e_cheese=="y":
        bill+=1
    print(f"your bill is {bill} ")
elif size=="m":
    bill=20
    if pepparoni=="y":
        bill+=3
    if e_cheese=="y":
        bill+=1
    print(f"your bill is {bill} ")
else:
    bill=25
    if pepparoni=="y":
        bill+=3
    if e_cheese=="y":
        bill+=1
    print(f"your bill is {bill} ")
    
