import time

candy = int(0)
with_friend = False
alone = False
own_house = False
friend_house = False
costume = False
guilt = False
house_or_search = False
search1 = False
market_map = False
west1 = False
east1 = False
market1 = False
west1house = False
west2 = False
east1mall = False
east2 = False
west1house2 = False
west2 = False
goodanswer = False

print("(1) You go with your friend")
print("(2) You go home by yourself")
answer = input("Which one do you choose? ")

if answer == "1":
    with_friend = True
elif answer == "2":
    alone = True

while True:
    if alone == True:
        print("You go home by yourself")
        time.sleep(1)
        print("A day passes, and you are back in school")
        time.sleep(1)
        print("You realize that you don't see your friend is in school")
        time.sleep(1)
        print("After the school is over, you go to your own house")
        time.sleep(1)
        print("When you open a newspaper, you see that your friend has gone missing")
        time.sleep(1)
        while goodanswer == False:
            print("(1) You decide to search for your friend")
            print("(2) You decide to go trick and treating")
            answer = input("Which one do you choose? ")
            if answer == "1":
                costume = True
                alone = False
                goodanswer = True
            elif answer == "2":
                guilt = True
                alone = False
                goodanswer = True
            else:
                print("Invalid Answer")


    if guilt == True:
        print("You decide to go trick or treating")
        time.sleep(1)
        print("You just ignore your missing friend, and have a normal Halloween")
        time.sleep(1)
        print("You live with the guilt that you didn't search for a missing friend")
        time.sleep(2)
        print("GUILT ENDING")
        guilt = False

    if costume == True:
        goodanswer = False
        print("You decide to act like going trick or treating to ask neightboring houses")
        time.sleep(1)
        while goodanswer == False:
            print("(1) You wear a ghost costume")
            print("(2) You wear a superhero costume")
            print("(3) You wear an apple costume")
            print("(4) You wear a cat costume")
            answer = input("Which one do you choose? ")
            if answer == "1":
                print("You wear the ghost costume")
                ghost_costume = True
                search1 = True
                costume = False
            elif answer == "2":
                print("You wear the superhero costume")
                search1 = True
                costume = False
            elif answer == "3":
                print("You wear the apple costume")
                search1 = True
                costume = False
            elif answer == "4":
                print("You wear a cat costume")
                search1 = True
                costume = False
            else:
                print("Invalid Answer")

    if search1 == True:
        print("After choosing your costume, you get out of your house")
        time.sleep(1)
        print("(1) Go to your missing friend's house")
        print("(2) Go to the school")
        print("(3) Go to your old lady's house")
        print("(4) Go to the mall")
        print("(5) Go to the park")
        print("(6) Go to the haunted house")
        if market_map == True:
            print("(7) Go to the market")
        answer = input("Which one do you choose? ")
        if answer == "1":
            friend_house = True