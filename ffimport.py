class character:
    def __init__(self, health):
        self.health = int(health)

    def gethealth(self):
        return self.health

    def sethealth(self, finalhealth):
        self.health = finalhealth
        return self.health

    def zerohealth(self):
        self.health = 0
        return self.health

class player(character):
    def __init__(self, health, name, inventory):
        super().__init__(health)
        self.name = name
        self.inventory = inventory

    def pickupitem(self, item):
        self.inventory.append (item)
        return self.inventory


    def removeitem(self, item):
        self.inventory.remove(item)
        return self.inventory

    def getinventory(self):
        return self.inventory

    def getname(self):
        return self.name

class enemy(character):
    def __init__(self,health, type, power, weapon, damage):
        super().__init__(health)
        self.type = type
        self.power = power
        self.weapon = weapon
        self.damage = damage

    def getpower(self):
        return self.power

    def getweapon(self):
        return self.weapon

    def getdamage(self):
        return self.damage

    def damageplayer(self, armour, player1, free):
        power = 0
        x = 0
        if self.type == "type1":
            power = self.damage


        elif self.type == "type2":
            power = self.damage
            print(power)


        elif self.type == "type3":
            power = self.damage


        elif self.type == "rboss":
            power = self.damage

        elif self.type == "bboss":
            power = self.damage
            import random
            choice = random.randint(1,4)
            if choice == 1:
                power = power * 1.5
                print("The boss has used their super strength ability and hit your 1.5x damage!!")


        elif self.type == "gboss":
            power = self.damage
            import random
            chance = random.randint(1,4)
            if chance == 1:
                print("You have been poisoned!!")
                potion = int(input("Enter 1 if you have a magic potion to disable the potion: "))
                if potion == 1:
                    inventory = player1.getinventory()
                    for y in inventory:
                        if y == "magic potion":
                            print("Poison cured")
                            power = 0
                            break


                else:
                    import time
                    for i in range(5, 0, -1):
                        print('Poisoned for 5 damage')
                        time.sleep(i)
                        power = 25


        elif self.type == "finalboss":
            power = self.damage
            if free == False:
                import random
                chance = random.randint(1,4)
                if chance == 1:
                    print("You have been poisoned!!")
                    potion = int(input("Enter 1 if you have a magic potion to disable the potion: "))
                    if potion == 1:
                        inventory = player1.getinventory()
                        for y in inventory:
                            if y == "magic potion":
                                print("Poison cured")
                                power  = 0
                                break
                            else:
                                print ("You do not have the correct equipment")
                    else:
                        import time
                        for i in range(5, 0, -1):
                            print('Poisoned for 5 damage')
                            time.sleep(i)
                            power = 25
                if chance == 2:
                    power = power * 1.5
                    print("The boss has used their super strength ability and hit your 1.5x damage!!")


        if armour == True:
            reduction = power / 5
            power -= reduction
        x = player1.gethealth()
        x -= power
        x = int(x)
        if x <= 0:
            player1.zerohealth()
        elif x > 0:
            finalhealth = x
            player1.sethealth(finalhealth)

class item:
    def __init__(self, name,armour):
        self.name = name
        self.armour = armour

    def getarmour(self):
        return self.armour



