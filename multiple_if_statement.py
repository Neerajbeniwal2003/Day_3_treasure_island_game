#NOW talking about multiple if statement
#for example:-
# if the person height is greater then 120 then they are allowed to take a ride
#and make the different prizes for different age groups
#and ask if they want to take photos or not if ther say yes then add $3 to the total prize
print("welcome to roler coster")
height=int(input("what is your height:"))
bill=0
if height > 120:
    age=int(input("what is your age:"))
    if age <12:
        bill=5
    elif age>=12 and age<=18:
        bill=7
    else:
        bill=12
    want_photos=input("do you want photos or not type y for yes and n for no:")
    if want_photos == "y":
        bill+=3 #it means bill = bill+3
        print(f"your bill is ${bill}") 
else:
    print("you are not eligible")