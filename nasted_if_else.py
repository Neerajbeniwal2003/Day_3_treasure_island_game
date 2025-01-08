#In nested if else statement 
#there is another if else statement in if statement 

#for example
# if the person height is greater then 120 then they are allowed to take a ride
print("welcome to roler coster")
height=int(input("what is your height:"))
if height > 120:
    age=int(input("what is your age:"))
    if age <=18:
        print("you can pay $7.")
    else:
        print("you can pay $18.")
else:
    print("you are not eligible")


#if elif else statement

#for example
# if the person height is greater then 120 then they are allowed to take a ride
#make the different prizes for different age groups
print("welcome to roler coster")
height=int(input("what is your height:"))
if height > 120:
    age=int(input("what is your age:"))
    if age <12:
        print("you can pay $5.")
    elif age>=12 and age<=18:
        print("plese pay $7.")
    else:
        print("please pay $12.")
    
else:
    print("you are not eligible")






