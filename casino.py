# coding=utf-8


class Casino():
    def __init__(self):
        pass

    # Todo: Adapt code to new object structure
    # self.gamble_active = True
    # if (self.player.money < 3500):
    #    print('\nSorry, you don\'t have enough money to enter the casino, you need a minimum of 3500$\n')
    # else:
    #    while self.gamble_active:
    #        if self.first_time_gamble:
    #            print(self.first_time_gamble_message)
    #            self.first_time_gamble = False
    #        gamble_option = input('Enter your option, or type "help" for gamble help message> ')
    #        if gamble_option == 'help':
    #            print(self.first_time_gamble_message)
    #        elif gamble_option == 'flip':
    #            try:
    #                amount_to_gamble = int(input('How much money do you want to gamble? (enter numbers only)> '))
    #                if not amount_to_gamble > self.player.money:
    #                    side = input(
    #                        'Enter what coin side you bet it will land on? ("ferrari side" or "dollar side")> ')
    #                    os.system('clear')
    #                    if (side == 'ferrari side') or (side == 'dollar side'):
    #                        random_number = random.randint(1, 1000)
    #                        if (random_number < 501):
    #                            winning_coin_side = 'ferrari side'
    #                        else:
    #                            winning_coin_side = 'dollar side'
    #                        if winning_coin_side == side:
    #                            print('\nCongrats, you won ' + str(amount_to_gamble) + '$')
    #                            self.player.money += amount_to_gamble
    #                            self.player.xp += 50
    #                            self.player.update_level()
    #                            print('\nYour xp has been increased by 50\n' + str(
    #                                self.player.xp_required - self.player.xp) + 'xp to level up\nCurrent money is ' + str(
    #                                self.player.money) + '$\n')
    #                        else:
    #                            print('\nCrap, you lost ' + str(amount_to_gamble) + '$')
    #                            self.player.money -= amount_to_gamble
    #                            self.player.xp += 25
    #                            self.player.update_level()
    #                            print('\nYour xp has been increased by 25\n' + str(
    #                                self.player.xp_required - self.player.xp) + 'xp to level up\nCurrent money is ' + str(
    #                                self.player.money) + '$\n')
    #                        replay = input('Do you want to gamble more? (y/n)> ')
    #                        if replay == ('y'):
    #                            pass
    #                        elif replay == ('n'):
    #                            self.gamble_active = False
    #                    else:
    #                        print('Oops you entered a invalid side!\n')
    #                else:
    #                    print('You don\'t have enough money!')
    #            except ValueError:
    #                print('Invalid answer...')
    #        elif gamble_option == 'roll':
    #            try:
    #                amount_to_gamble = int(input('How much money do you want to gamble? (enter numbers only)> '))
    #                if not amount_to_gamble >= self.player.money:
    #                    chosen_number = int(input('Choose what number you think you\'ll get (2-12)>'))
    #                    os.system('clear')
    #                    if not chosen_number in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
    #                                             12]:  # (chosen_number > 12 or chosen_number < 1):
    #                        print('You didn\'t enter a valid number!')
    #                    else:
    #                        number_roll_one = random.randint(1, 6)
    #                        number_roll_two = random.randint(1, 6)
    #                        number_result = number_roll_one + number_roll_two
    #                        if chosen_number == number_result:
    #                            self.player.money += 12 * amount_to_gamble
    #                            self.player.xp += 125
    #                            self.player.update_level()
    #                            print('Congrats you won ' + str(
    #                                amount_to_gamble * 12) + '$\nYour xp has been increased by 125\n' + str(
    #                                self.player.xp_required - self.player.xp) + 'xp to level up\nCurrent money is ' + str(
    #                                self.player.money) + '$\n')
    #                        else:
    #                            self.player.money -= amount_to_gamble
    #                            self.player.xp += 25
    #                            self.player.update_level()
    #                            print('Crap, you lost ' + str(
    #                                amount_to_gamble) + '$\nYour xp has been increased by 25\n' + str(
    #                                self.player.xp_required - self.player.xp) + 'xp to level up\nCurrent money is ' + str(
    #                                self.player.money) + '$\n')
    #                        print('You rolled a total of ' + str(number_result) + ' (' + str(
    #                            number_roll_one) + ' and ' + str(number_roll_two) + ')')
    #                        replay = input('\nDo you want to gamble more? (y/n)> ')
    #                        if replay == ('y'):
    #                            pass
    #                        elif replay == ('n'):
    #                            self.gamble_active = False
    #                else:
    #                    print('You don\'t have enough money!')
    #            except ValueError:
    #                print('Invalid answer...')
    #        elif gamble_option == ('exit'):
    #            self.gamble_active = False
    #        else:
    #            print('\n\nInvalid command, type "help" to see all commands.\n')