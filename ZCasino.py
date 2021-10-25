import os
from random import randrange
from math import ceil
#Parameter instanciation
argent=1000
continuer_partie=True

print("This is the famous roulette game of a casino")
while continuer_partie:
    temp=-1
    while temp<0 or temp>49:
        temp= input("Choose an integer between 0 and 49\n")
        try:
            temp=int(temp)
        except ValueError:
            print("You did not type an integer")
            temp=-1
            continue
        if temp<0:
            print("This is a negative integer")
        if temp>49:
            print("This is an integer bigger than 49")

    mise=0
    while mise<=0 or mise>argent :
        mise=input("Enter the amount you want to bet : ")
        try:
            mise=int(mise)
        except ValueError:
            print("You did not type a correct integer")
            mise=-1
            continue
            if mise<=0:
                print("Your bet is negative or null")
            if mise>argent:
                print("You are authorised to bet just",argent,"$")
    print ("You choosed to bet ", mise, "$ on number ", temp )
    win=randrange(50)
    if (win==temp) :
        print ("Congratulations :). THe roulette stopped on ", win ,". Therefore you win three time the betting amount which equalas to ", ceil(mise + (mise*3)) ,"$\n")
        argent = ceil(mise + (mise*3))
    elif ((win%2)==(temp%2)) :
        print ("Congratulations :). THe roulette stopped on ", win ,", which has the same color as the number you choosed. Therefore you win half of the betting amount which equalas to ", ceil(mise + (mise*0.5)) ,"$")
        argent= ceil(mise + (mise*0.5))
    else :
        print ("The roulette stopped on", win, "Sorry. You had no chance. You loose. See you on another day :)")
        argent-=mise
    if argent<=0:
        print("You are ruined. You can not bet")
        continuer_partie=False
    else:
        print("You have now",argent,"$")
        quitter=input("Do you wish to leave the Casino ? (y/n) ? ")
        if quitter=="o"or quitter=="O":
            print("You leave the Casino with gains.")
            continuer_partie=False
os.system("pause")