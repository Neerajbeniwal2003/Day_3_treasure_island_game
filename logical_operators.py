#logical operators are
# and ,or ,not
#for example
#A and B-in this if both the A , B are true then the value is consider to be true
#A and B-if one of then if false then the whole output will be false

#A or B- if any one of them is true then the output will also true
#A or B- it if only false when both of the A,B are false

#not A - it is use for reversing the codition
#so when the condition is false it become true 
#and if the condition is true it become false

#now taking a code example 
#update the code so that the age 45 to 55 will get the ride for free
print("welcome to roler coster")
height=int(input("what is your height:"))
bill=0
if height > 120:
    age=int(input("what is your age:"))
    if age <12:
        bill=5
    elif age>=12 and age<=18:
        bill=7
    elif age>=44 and age <=55:
        bill=0
    else:
        bill=12
    want_photos=input("do you want photos or not type y for yes and n for no:")
    if want_photos == "y":
        bill+=3 #it means bill = bill+3
        print(f"your bill is ${bill}") 
else:
    print("you are not eligible")