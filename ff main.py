from ffimport import player, enemy, item
import sys
reddeath = 0
bluedeath = 0
greendeath = 0
strength = False
superS = False
armour1 = item("placeholder", False)

def playersetup():
    inventory = []
    name = input("Please enter your username: ")
    health = 100
    player1 = player(health, name, inventory)
    playermove(player1)


def playermove(player1):
    minion1 = enemy(100,"type1",5,"assault rifle",25)
    minion2 = enemy(110,"type2",7,"ninja shurikens", 35)
    minion3 = enemy(125,"type3",10,"minigun", 40)
    health = player1.gethealth()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("current health: ",health)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    while health > 0 :
        line = 0
        choice = input("Enter 1 to access your inventory: ")
        if choice == "1":
            accessinventory(player1)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        import time
        time.sleep(1)
        file = open ("movement.txt","r")
        filecontents = file.readlines()
        import random
        randommove = int (random.uniform(1,22))
        chosenline = line + randommove
        movement = filecontents [chosenline].strip()
        file.close()
        msplit = movement.split(" ")
        types = msplit[0]
        event = msplit[1].strip()
        if event == "potion":
            potiontypes(event,types,player1)
        elif event == "door":
            doortypes(event, types, player1)
        elif event == "key":
            keytypes(event, types, player1)
        elif event == "armour":
            armourtypes(event, types )
        elif event == "field":
            forcefield(player1)
        elif event == "minion":
            miniontypes(player1,types,  minion1, minion2, minion3)
        if health <= 0:
            death(player1)





def potiontypes(event, types, player1):
    if types == "healing":
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("You have found a healing potion")
        use = int(input("Enter 1 to heal and 2 to pickup: "))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        if use == 1:
            player1.sethealth(125)
            print("You are now on {}".format(player1.gethealth()))
            health = player1.gethealth()
            print (health)
        elif use == 2:
            item = types + " " + event
            player1.pickupitem(item)
            inventory = player1.getinventory()
            print(inventory)
    if types == "strength":
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("You have found a strength potion")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Once you use it, you will permanently have strength which increases your number range by 2")
        use = int(input("Enter 1 to use and 2 to pickup: "))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        if use == 1:
            global strength
            strength = True
        elif use == 2:
            item = types + " " + event
            player1.pickupitem(item)
            inventory = player1.getinventory()
            print(inventory)
    if types == "magic":
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("You have found a magic potion")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        item = types + " " + event
        player1.pickupitem(item)
        inventory = player1.getinventory()
    if reddeath >= 1 and bluedeath >= 1 and greendeath >=1:
        finalboss(player1)
    else:
        playermove(player1)


def doortypes(event, types, player1):
    key = False
    redboss = enemy(150,"rboss",12,"increased damage",50)
    blueboss = enemy(150,"bboss",12,"forcefield",50)
    greenboss = enemy(150,"gboss",12,"poison",50)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    if types == "red":
        print("You have found the red door")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        use = int(input("Enter 1 to use a red key if you have one: "))
        if use == 1:
            inventory = player1.getinventory()
            for x in inventory:
                if x == "red key":
                    player1.removeitem("red key")
                    redbossfight(player1, redboss)
                    key = True
            if key == False:
                print ("You do not have the key")
    elif types == "blue":
        print("You have found the blue door")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        use = int(input("Enter 1 to use a blue key if you have one: "))
        if use == 1:
            inventory = player1.getinventory()
            for x in inventory:
                if x == "blue key":
                    player1.removeitem("blue key")
                    bluebossfight(player1, blueboss)
                    key = True
            if key == False:
                print ("You do not have the key")
    elif types == "green":
        print("You have found the green door")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        use = int(input("Enter 1 to use a green key if you have one: "))
        if use == 1:
            inventory = player1.getinventory()
            for x in inventory:
                if x == "green key":
                    player1.removeitem("green key")
                    greenbossfight(player1, greenboss)
                    key = True
            if key == False:
                print ("You do not have the key")
    playermove(player1)


def keytypes(event, types, player1):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    item = types + " " + event
    player1.pickupitem(item)
    inventory = player1.getinventory()
    print("You have obtained {}".format(item))
    playermove(player1)

def armourtypes(event, types ):
    global armour1
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    x = types + " " + event
    armour1 = item(x,True)
    print("You have got armour!")


def forcefield(player1):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("You have discovered a forcefield")
    use = int(input("Enter 1 to use the potion: "))
    if use == 1:
        inventory = player1.getinventory()
        for x in inventory:
            if x == "magic potion":
                print("Forcefield disabled")
                print("You have acquired a strength potion")
                player1.pickupitem("strength potion")
                player1.removeitem("magic potion")
                playermove(player1)
            else:
                print ("You do not have the correct equipment")



def miniontypes(player1,types,  minion1, minion2, minion3):
    global strength
    global armour1
    free = False
    x = 10
    if strength == True:
        x += 2
    print ("You have found a minion")
    if types == "type1":
        enemyh = minion1.gethealth()
        power = minion1.getpower()
    elif types == "type2":
        enemyh = minion2.gethealth()
        power = minion1.getpower()
    elif types == "type3":
        enemyh = minion3.gethealth()
        power = minion1.getpower()
    while enemyh > 0 or healthp > 0:
        import random
        enemynumber = random.randint(0,power)
        playernumber = random.randint(0,x)
        print("#######################################")
        print("Your number is: ",playernumber)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Enemy number is: ",enemynumber)
        print("#######################################")
        armour = armour1.getarmour()
        import time
        time.sleep(2)
        if enemynumber > playernumber:
            print("you took damage")
            if types == "type1":
                damage = minion1.damageplayer(armour, player1, free)
                healthp = player1.gethealth()
                mhealth = minion1.gethealth()
                print("Your health: ",healthp)
                print("Minions health: ",mhealth)
            elif types == "type2":
                damage = minion2.damageplayer(armour, player1, free)
                healthp = player1.gethealth()
                mhealth = minion1.gethealth()
                print("Your health: ",healthp)
                print("Minions health: ",mhealth)
            elif types == "type3":
                damage = minion3.damageplayer(armour, player1, free)
                healthp = player1.gethealth()
                mhealth = minion1.gethealth()
                print("Your health: ",healthp)
                print("Minions health: ",mhealth)
        if playernumber > enemynumber:
            if types == "type1":
                damage = minion1.sethealth(0)
                print("You have won")
                playermove(player1)
            elif types == "type2":
                damage = minion2.sethealth(0)
                print("You have won")
                playermove(player1)
            elif types == "type3":
                damage = minion3.sethealth(0)
                print("You have won")
                playermove(player1)
        healthp = player1.gethealth()
        if healthp <= 0:
            death(player1)

def accessinventory(player1):
    inventory = player1.getinventory()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(inventory)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    number = int(input("""Please enter the number slot of the item you want to select.
    First Slot = 1
    Second Slot = 2... etc
    Enter 0 to exit
    """))
    if number == 0:
        finalboss(player1)
    chosenitem = inventory[number-1]
    itemsplit = chosenitem.split(" ")
    types = itemsplit[0]
    event = itemsplit[1].strip()
    if types == "healing":
        player1.sethealth(125)
        print("You are now on {}".format(player1.gethealth()))
        health = player1.gethealth()
        print (health)
        player1.removeitem("healing potion")
    if types == "strength":
        global strength
        strength = True
        print("You have enabled strength")
        player1.removeitem("strength potion")




def death(player1):
    print("{} has died. Unlucky!".format(player1.getname()))
    sys.exit()



def bluebossfight(player1, blueboss):
    free = False
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("You have found the blue boss!")
    print("""Its number range is up to 12 and does 50 damage per hit and has 150 health
This is the blue boss so it has a special 1.5x damage attack(25% chance) so be careful!
    """)
    global strength
    global armour1
    x = 10
    playerpower = 50
    if strength == True:
        x += 2
    healthp = player1.gethealth()
    bosshealth = blueboss.gethealth()
    power = blueboss.getpower()
    while bosshealth > 0 or healthp > 0:
        import random
        enemynumber = random.randint(0, power)
        playernumber = random.randint(0, x)
        print("#######################################")
        print("Your number is: ",playernumber)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Enemy number is: ",enemynumber)
        print("#######################################")
        armour = armour1.getarmour()
        import time
        time.sleep(2)
        if enemynumber > playernumber:
            print("You lost this round and you took damage")
            damage = blueboss.damageplayer(armour, player1, free)
            healthp = player1.gethealth()
            bosshealth = blueboss.gethealth()
            print("Your health: ",healthp)
            print("Bosses health: ",bosshealth)
        elif playernumber > enemynumber:
            bosshealth -= playerpower
            damage = blueboss.sethealth(bosshealth)
            print("You have won this round")
            healthp = player1.gethealth()
            bosshealth = blueboss.gethealth()
            print("Your health: ",healthp)
            print("Bosses health: ",bosshealth)
        healthp = player1.gethealth()
        bosshealth = blueboss.gethealth()
        import time
        time.sleep(3)
        if healthp <= 0:
            death(player1)
        if bosshealth <= 0:
            print("You have defeated the mini boss")
            player1.sethealth(175)
            print("You have got 175 health now, preparing you for your final fight soon ")
            global bluedeath
            bluedeath += 1
            finalboss(player1)
            playermove(player1)

def redbossfight(player1, redboss):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("You have found the red boss!")
    print("""Its number range is up to 12 and does 50 damage per hit and has 150 health
This is the red boss so it has a special forcefield defence(25% chance), so dont get your hopes up too much when you win a round!
    """)
    free = False
    global strength
    global armour1
    x = 10
    playerpower = 50
    if strength == True:
        x += 2
    healthp = player1.gethealth()
    bosshealth = redboss.gethealth()
    power = redboss.getpower()
    while bosshealth > 0 or healthp > 0:
        import random
        enemynumber = random.randint(0, power)
        playernumber = random.randint(0, x)
        print("#######################################")
        print("Your number is: ",playernumber)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Enemy number is: ",enemynumber)
        print("#######################################")
        armour = armour1.getarmour()
        import time
        time.sleep(2)
        if enemynumber > playernumber:
            print("You lost this round and you took damage")
            damage = redboss.damageplayer(armour, player1, free)
            healthp = player1.gethealth()
            bosshealth = redboss.gethealth()
            print("Your health: ",healthp)
            print("Bosses health: ",bosshealth)
        elif playernumber > enemynumber:
            import random
            chance = random.randint(1,3)
            if chance == 1:
                damage = redboss.sethealth(bosshealth)
                print("Your attack has been blocked by the minibosses forcefield!!")
            else:
                bosshealth -= playerpower
                damage = redboss.sethealth(bosshealth)
                print("You have won this round")
                healthp = player1.gethealth()
                bosshealth = redboss.gethealth()
                print("Your health: ",healthp)
                print("Bosses health: ",bosshealth)
        healthp = player1.gethealth()
        bosshealth = redboss.gethealth()
        import time
        time.sleep(3)
        if healthp <= 0:
            death(player1)
        elif bosshealth <= 0:
            print("You have defeated the mini boss")
            print("You have gained permanent super strength, your number range is up to 17!")
            global reddeath
            global superS
            superS = True
            reddeath += 1
            finalboss(player1)
            playermove(player1)

def greenbossfight(player1, greenboss):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("You have found the green boss!")
    print("""Its number range is up to 12 and does 50 damage per hit and has 150 health
This is the green boss so it has a special poison attack(25% chance) be careful!
    """)
    free = False
    global strength
    global armour1
    x = 10
    playerpower = 50
    if strength == True:
        x += 2
    healthp = player1.gethealth()
    bosshealth = greenboss.gethealth()
    power = greenboss.getpower()
    while bosshealth > 0 or healthp > 0:
        import random
        enemynumber = random.randint(0, power)
        playernumber = random.randint(0, x)
        print("#######################################")
        print("Your number is: ",playernumber)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Enemy number is: ",enemynumber)
        print("#######################################")
        armour = armour1.getarmour()
        import time
        time.sleep(2)
        if enemynumber > playernumber:
            print("You lost this round and you took damage")
            damage = greenboss.damageplayer(armour, player1, free)
            healthp = player1.gethealth()
            bosshealth = greenboss.gethealth()
            print("Your health: ",healthp)
            print("Bosses health: ",bosshealth)
        elif playernumber > enemynumber:
            print("You have won this round")
            bosshealth -= playerpower
            damage = greenboss.sethealth(bosshealth)
            healthp = player1.gethealth()
            bosshealth = greenboss.gethealth()
            print("Your health: ",healthp)
            print("Bosses health: ",bosshealth)
        import time
        time.sleep(3)
        healthp = player1.gethealth()
        bosshealth = greenboss.gethealth()
        import time
        time.sleep(3)
        if healthp <= 0:
            death(player1)
        if bosshealth <= 0:
            print("You have defeated the mini boss")
            global greendeath
            greendeath += 1
            finalboss(player1)
            playermove(player1)



def finalboss(player1):
    global reddeath
    global bluedeath
    global greendeath
    free = False
    final = enemy(200, "finalboss", 15, "themselves", 65)
    if reddeath >= 1 and bluedeath >= 1 and greendeath >=1:
        print("Initiating final boss fight...")
        import time
        time.sleep(1)
        print("Loading...")
        time.sleep(1)
        print("You should probably make sure you are prepared...")
        inventory = player1.getinventory()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(inventory)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        number = int(input("""Please enter the number slot of the item you want to select.
        First Slot = 1
        Second Slot = 2... etc
        Enter 0 to exit
        """))
        if number != 0:
            chosenitem = inventory[number-1]
            itemsplit = chosenitem.split(" ")
            types = itemsplit[0]
            event = itemsplit[1].strip()
            if event == "potion":
                potiontypes(event,types,player1)

        global strength
        global armour1
        x = 10
        playerpower = 50
        if superS == True:
            x += 7
        healthp = player1.gethealth()
        bosshealth = final.gethealth()
        armour = armour1.getarmour()
        power = final.getpower()
        while bosshealth > 0 or healthp > 0:
            free = False
            import random
            r = random.randint(1,4)
            if r == 1:
                free = True
                print("The boss has teleported behind you before you could react")
                print("You took {} damage".format(final.getdamage()))
                damage = final.damageplayer(armour, player1, free)
                healthp = player1.gethealth()
                bosshealth = final.gethealth()
                print("Your health: ",healthp)
                print("Bosses health: ",bosshealth)
                if healthp <= 0:
                    death(player1)
            import random
            enemynumber = random.randint(0, power)
            playernumber = random.randint(0, x)
            print("#######################################")
            print("Your number is: ",playernumber)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Enemy number is: ",enemynumber)
            print("#######################################")
            import time
            time.sleep(2)
            if enemynumber > playernumber:
                print("You lost this round and you took damage")
                damage = final.damageplayer(armour, player1,free)
                healthp = player1.gethealth()
                bosshealth = final.gethealth()
                print("Your health: ",healthp)
                print("Bosses health: ",bosshealth)
            elif playernumber > enemynumber:
                import random
                chance = random.randint(1,5)
                if chance == 1:
                    damage = final.sethealth(bosshealth)
                    print("Your attack has been blocked by the minibosses forcefield!!")
                    healthp = player1.gethealth()
                    bosshealth = final.gethealth()
                    print("Your health: ",healthp)
                    print("Bosses health: ",bosshealth)
                else:
                    print("You have won this round")
                    bosshealth -= playerpower
                    damage = final.sethealth(bosshealth)
                    healthp = player1.gethealth()
                    bosshealth = final.gethealth()
                    print("Your health: ",healthp)
                    print("Bosses health: ",bosshealth)
            healthp = player1.gethealth()
            bosshealth = final.gethealth()
            import time
            time.sleep(3)
            if healthp <= 0:
                death(player1)
            if bosshealth <= 0:
                print("You have defeated the final boss")
                endcredits(player1)

    else:
        playermove(player1)


def endcredits(player1):
    print("""I see the player you mean...

{}?

Yes. Take care. It has reached a higher level now. It can read our thoughts...

As if it is words on a screen...

I like this player. It played well. It did not give up...

I agree...

Use its name...

{}. Player of games...

And the universe said you have played the game well...

And the universe said everything you need is within you...

And the universe said you are stronger than you know...

You are the player...

Well Done.""". format(player1.getname(),player1.getname()))
    import sys
    sys.exit()





playersetup()
