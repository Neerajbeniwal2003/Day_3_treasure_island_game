print("welcome to the treasure island \nyour mission is to fine the treasure")
step1=input("you are at a cross road ,where do you wanna go\n type 'right'or 'left:")
if step1=="left":
    step2=input("swim or wait:")
    if step2=="wait":
        step3=input("which door?red,yellow or blue:")
        if step3=="red":
            print("burned by a fire\n game over")
        elif step3=="yellow":
            print("you win")
        elif step3=="blue":
            print("eaten by a beast \n game over")
        else:
            print("game over")
    else:
        print("attacked by trout\n game over")
else:
    print("fall into a hole\n game over")



