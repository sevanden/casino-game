import time, random, os, save #save is a costum made module

helpmsg = """\n
earn            earns income money for 2 minutes
help            shows all options
save            saves your player's info
clear           clears the screen
exit            saves and then exits the program
force_exit      forces the program to stop
gamble          gamble your money
buy             to buy properties (in progress)
stats           view your stats (money, level, etc)
property_stats  view your property stats (what is owned, what is unlocked when, etc)
---all bought properties will be hired by others, increasing your income, you have a simple house for hire when you start for base income of 1800$, more properties equals more loan, have fun ;)---\n"""
gamblemsg = """\n
Hello there, this is the casino where you can gamble, there are three gamble options:
    coinflip
    roll and dice
Type 'flip' for coinflip \nType 'roll' for roll and dice\nType 'exit' if you want to stop gambling!\n"""

class Player:
    def __init__(self):
        self.money = 18000
        self.level = 1
        self.xp = 0
        self.income = 1800
        self.xp_required = 50*self.level
        self.properties = []
        self.properties_owned = 1
        self.data_to_save = []
        self.name = ""
    def update_level(self):
        while (self.xp >= self.xp_required):
            self.xp -= self.xp_required
            self.level += 1
            self.xp_required = 100*(self.level/2)
            self.money += 500*self.level
            print("\nYou've reached level " + str(self.level) + "!\nYou've been awarded " + str(500*self.level) + "$\nCurrent money is " + str(self.money) + "$\n\n")
            self.update_property_status()
    def loan(self):
        if (time.time() - game.start_time) > 15:
            game.start_time = time.time()
            self.money += self.income #base income
            self.xp += 25
            print("\nCurrent money is " + str(self.money) + "$")
    def update_property_status(self):
        for prop in self.properties:
            if (not prop.unlocked) and (self.level >= prop.unlocked_at):
                prop.unlocked = True
                print("You have unlocked a new item! (" + prop.name + ")")
    def view_properties(self):
        print("\nProperties:")
        for prop in self.properties:
            if prop.owned:
                print(prop.name + ": owned")
            elif prop.unlocked:
                print(prop.name + ": unlocked   (" + str(prop.price) + "$)")
            else:
                print(prop.name + ": locked   (unlocked at level " + str(prop.unlocked_at) + ")   (" + str(prop.price) + "$)")
        print("\n")
    def buy_property(self):
        self.view_properties()
        what_to_buy = raw_input("Enter the name of what you want to buy or type 'exit'(for example 'big house')> ")
        property_exists = 0
        if what_to_buy == "exit":
            pass
        else:
            for prop in self.properties:
                if what_to_buy == prop.name:
                    property_exists += 1
                    if not prop.unlocked:
                        print("\nProperty " + prop.name + " not unlocked yet, unlocked at level " + str(prop.unlocked_at) + "\n")
                    elif not player.money >= prop.price:
                        print("\nNot enough money, you have " + str(player.money) + "/" + str(prop.price) + "$\n")
                    elif prop.owned:
                        print("\nYou already own this property!\n")
                    else:
                        player.money -= prop.price
                        prop.owned = True
                        self.properties_owned += 1
                        self.income += prop.loan_increase
                        print("\nCongrats, you have successfully bought your property " + prop.name + "!\nCurrent money is " + str(player.money) + "$\nYour income has increased by " + str(prop.loan_increase) + "$ (current loan is " + str(player.income) + "$)\n")
            if property_exists == 0:
                print("\nSorry but that property doesn't exist\n")
    def save(self):
        self.data_to_save = []
        self.data_to_save = [str(self.money), str(self.level), str(self.xp), str(self.xp_required), str(self.income), str(self.properties_owned), str(int(time.time() - game.run_time))]
        for prop in player.properties:
            self.data_to_save.append(str(int(prop.owned)))
            self.data_to_save.append(str(int(prop.unlocked)))
        save.save_data(self.data_to_save, self.name, "w")
    def load(self):
        failure = False
        try:
            save_file = open("save/" + self.name + ".dat", "r") 
            self.money = int(save_file.readline())
            self.level = int(save_file.readline())
            self.xp = int(save_file.readline())
            self.xp_required = int(save_file.readline())
            self.income = int(save_file.readline())
            self.properties_owned = int(save_file.readline())
            game.run_time -= int(save_file.readline())
            for prop in self.properties:
                prop.owned = bool(int(save_file.readline()))
                prop.unlocked = bool(int(save_file.readline()))
            save_file.close()
        except IOError:
            print("\nSorry but that file doesn't exist, check if you spelled the name right (capitals, spaces, etc)\n")
            failure = True
        except ValueError:
            print("\nSorry but something went wrong when trying to read the save file\n")
            failure = True
        return failure
class Property:
    def __init__(self, kind, owned, unlocked, unlocked_at, price, name, loan_increase):
        self.kind = kind
        self.owned = owned
        self.unlocked = unlocked
        self.unlocked_at = unlocked_at
        self.price = price
        self.name = name
        self.loan_increase = loan_increase
        player.properties.append(self)
class GamingLoop:
    def __init__(self, helpmsg):
        self.start_time = time.time()
        self.run_time = time.time()
        self.disabled_time = 0
        self.helpmsg = helpmsg
        self.first_time_gamble_message = gamblemsg
        self.first_time_gamble = True
        self.console_active = True
        self.invalid_profile_option = True
    def gamble(self):
        self.gamble_active = True
        if (player.money<3500):
            print("\nSorry, you don't have enough money to enter the casino, you need a minimum of 3500$\n")
        else:
            while self.gamble_active:
                if self.first_time_gamble:
                    print(self.first_time_gamble_message)
                    self.first_time_gamble = False
                gamble_option = raw_input("Enter your option, or type 'help' for gamble help message> ")
                if gamble_option == "help":
                    print(self.first_time_gamble_message)
                elif gamble_option == "flip":
                    try:
                        amount_to_gamble = int(raw_input("How much money do you want to gamble? (enter numbers only)> "))
                        if not amount_to_gamble > player.money:
                            side = raw_input("Enter what coin side you bet it will land on? ('ferrari side' or 'dollar side')> ")
                            os.system("clear")
                            if (side=="ferrari side") or (side=="dollar side"):
                                random_number = random.randint(1,1000)
                                if (random_number < 501):
                                    winning_coin_side = "ferrari side"
                                else:
                                    winning_coin_side = "dollar side"
                                if winning_coin_side == side:
                                    print("\nCongrats, you won " + str(amount_to_gamble) + "$")
                                    player.money += amount_to_gamble
                                    player.xp += 50
                                    player.update_level()
                                    print("\nYour xp has been increased by 50\n" + str(player.xp_required - player.xp) + "xp to level up\nCurrent money is " + str(player.money) + "$\n")
                                else:
                                    print("\nCrap, you lost " + str(amount_to_gamble) + "$")
                                    player.money -= amount_to_gamble
                                    player.xp += 25
                                    player.update_level()
                                    print("\nYour xp has been increased by 25\n" + str(player.xp_required - player.xp) + "xp to level up\nCurrent money is " + str(player.money) + "$\n")
                                replay = raw_input("Do you want to gamble more? (y/n)> ")
                                if replay == ("y"):
                                    pass
                                elif replay == ("n"):
                                    self.gamble_active = False
                            else:
                                print("Oops you entered a invalid side!\n")
                        else:
                            print("You don't have enough money!")
                    except ValueError:
                        print("Invalid answer...")
                elif gamble_option == "roll":
                    try:
                        amount_to_gamble = int(raw_input("How much money do you want to gamble? (enter numbers only)> "))
                        if not amount_to_gamble >= player.money:
                            chosen_number = int(raw_input("Choose what number you think you'll get (2-12)>" ))
                            os.system("clear")
                            if not chosen_number in [1,2,3,4,5,6,7,8,9,10,11,12]:                 #(chosen_number > 12 or chosen_number < 1):
                                print("You didn't enter a valid number!")
                            else:
                                number_roll_one = random.randint(1,6)
                                number_roll_two = random.randint(1,6)
                                number_result = number_roll_one + number_roll_two
                                if chosen_number == number_result:
                                    player.money += 12*amount_to_gamble
                                    player.xp += 125
                                    player.update_level()
                                    print("Congrats you won " + str(amount_to_gamble*12) + "$\nYour xp has been increased by 125\n" + str(player.xp_required - player.xp) + "xp to level up\nCurrent money is " + str(player.money) + "$\n")
                                else:
                                    player.money -= amount_to_gamble
                                    player.xp += 25
                                    player.update_level()
                                    print("Crap, you lost " + str(amount_to_gamble) + "$\nYour xp has been increased by 25\n" + str(player.xp_required - player.xp) + "xp to level up\nCurrent money is " + str(player.money) + "$\n")
                                print("You rolled a total of " + str(number_result) + " (" + str(number_roll_one) + " and " + str(number_roll_two) + ")")
                                replay = raw_input("\nDo you want to gamble more? (y/n)> ")
                                if replay == ("y"):
                                    pass
                                elif replay == ("n"):
                                    self.gamble_active = False
                        else:
                            print("You don't have enough money!")
                    except ValueError:
                        print("Invalid answer...")
                elif gamble_option == ("exit"):
                    self.gamble_active = False
                else:
                    print("\n\nInvalid command, type 'help' to see all commands.\n")
    def run(self):
        player.update_property_status()
        while True:
            player.loan()
            player.update_level()
            if self.console_active:
                command = raw_input("Enter option (type 'help' for all options)> ")
                if command == ("earn"):
                    self.console_active = False
                    self.disabled_time = time.time()
                elif command == ("help"):
                    print(self.helpmsg) #create or addapt variable helpmsg
                elif command == ("force_exit"):
                    confirm = raw_input("Are you sure you want to force the program to stop without saving? (y/n)> ")
                    if confirm == ("y"):
                        exit()
                elif command == ("gamble"):
                    game.gamble()
                elif command == ("buy"):
                    player.buy_property()
                elif command == ("stats"):
                    print("\n\nLevel: " + str(player.level) + "\n" + str(player.xp) + "xp/" + str(player.xp_required) + "xp\nMoney: " + str(player.money) + "$\nProperties owned: " + str(player.properties_owned) + "\nLoan: " + str(player.income) + "$")
                    run_time = int(time.time()) - int(game.run_time)
                    total_time = ""
                    total_houres = 0
                    total_minutes = 0
                    total_seconds = 0
                    while run_time >= 3600:
                        run_time -= 3600
                        total_houres += 1
                    while run_time >= 60:
                        run_time -= 60
                        total_minutes += 1
                    total_seconds += run_time
                    print("Time played: " + str(total_houres) + "h" + str(total_minutes) + "m" + str(total_seconds) + "s\n")
                elif command == ("property_stats"):
                    player.view_properties()
                elif command == ("exit"):
                    print("Saving file...")
                    player.save()
                    print("Exiting game...")
                    exit()
                elif command == ("save"):
                    print("Saving file...")
                    player.save()
                elif command == ("clear"):
                    os.system("clear")
                else:
                    print("Invalid answer")
            elif (time.time() - self.disabled_time) > 120:
                self.console_active = True


player = Player()
player.basic_house = Property("house", True, True, 1, 0, "simple house", 0)   #use as hint: print(player.properties[0].kind)
player.big_house = Property("house", False, False, 5, 375000, "big house", 2500)
player.basic_villa = Property("house", False, False, 10, 695000, "simple villa", 3000)
player.big_villa = Property("house", False, False, 15, 750000, "big villa", 5000)
player.basic_penthouse = Property("house", False, False, 20, 1000000, "simple penthouse", 7500)
player.big_penthouse = Property("house", False, False, 30, 1500000, "big penthouse", 40000)
player.castle = Property("castle", False, False, 50, 9000000, "caste", 120000)

game = GamingLoop(helpmsg)

print("Hello, welcome to my name gambling game\nHere you can gamble without losing real money\nAll you lose here is time, have fun!\n")
while game.invalid_profile_option:
    check_if_new = raw_input("Do you want to load a save file or create a new one? (load/create/exit)> ")
    if check_if_new == "load":
        player.name = str(raw_input("Enter your player / save file name> "))
        game.invalid_profile_option = player.load() #tries to load file, if successfully worked, it also returns False to get out of loop, incase error you can enter new filename
        if not game.invalid_profile_option:
            print("\nWelcome back " + player.name + "!\n")
    elif check_if_new == "create":
        player.name = str(raw_input("What is your name? (filename equals player name)> "))
        game.invalid_profile_option = save.create_file(player.name)
    elif check_if_new == "exit":
        exit()
    else:
        print("Sorry you didn't enter a valid option")

game.run()
