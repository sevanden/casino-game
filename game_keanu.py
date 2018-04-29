import pickle
import os

from player import Player
from market import Market
from bank import Bank
from casino import Casino


class Game():
    def __init__(self, playername, difficulty):
        self._status_message = ''                                                                                       # The game always starts with a blank status message.
        self.player = Player(playername)                                                                                # Create the player
        self.difficulty = difficulty                                                                                    # Set the game difficulty
        # Todo: create Level object with name, description, player targets to move on to the next level.
        self.current_level = 1                                                                                          # A new game always starts at Level 1
        self.xp_required = (self.difficulty * 50) * self.current_level                                                  # Requirements to reach the next level.
        # Todo: create GameTimer class for the following
        #   self.start_time = time.time()
        #   self.run_time = time.time()
        #   self.disabled_time = 0
        self.market = Market(self.current_level, self.player.xp)                                                        # The Market stuff where the user will buy things.
        self.bank = Bank()                                                                                              # The bank
        self.casino = Casino()                                                                                          # The casino where the user can waste his earnings.

    def __str__(self):
        l1 = 'Player: %s' % self.player.name
        l2 = 'Level: %d' % self.current_level
        l3 = 'Experience: %d' % self.player.xp
        l4 = '%s' % self.player.finance
        l5 = 'Message: %s' % self._status_message
        if self._status_message == '':
            return '%s - %s - %s - %s\n' % (l1, l2, l3, l4)
        else:
            return '%s - %s - %s - %s - %s\n' % (l1, l2, l3, l4, l5)

    def save(self):
        """Save the game (object) to file with name 'data/save/<self.player.name>.dat' """
        print('Saving game to data/save/%s.dat' % self.player.name)
        game_file = open('data/save/%s.dat' % self.player.name, 'bw')
        # Todo: Fix pickle error for class a_product or find workaround.
        pickle.dump(self, game_file)
        game_file.close()

    def _update_level(self):
        if self.player.xp >= int(self.xp_required):
            self.current_level += 1
            self.market.update_product_list(self.current_level, self.player.xp)

    def _update_userxp(self):
        self.player.xp += 1
        self.market.update_product_list(self.current_level, self.player.xp)

    def _status_line(self):
        os.system('clear')
        print(self)  # The status line containing level, player and other game stats.

    def _game_screen(self):
        self._status_line()
        self.player._list_assets()

    def _market(self):
        while True:
            self._status_line()
            print('The market - List of currently available products.')
            print('--------------------------------------------------')
            product_index = 0
            for product in self.market.get_product_list():
                print('%d - %s - %s - %s' % (product_index, product.asset.name, product.asset.description, product.asset.value))
                product_index += 1
            print('-' * 79)
            user_command = input('1) Buy 2) Leave the Market - Your choice: ')
            if user_command == '1':
                product_to_purchase = self.market.get_product_details(int(input('Enter the product-ID: ')))
                if product_to_purchase.value > self.player.finance.cash:
                    self._status_message = 'Insufficient funds to purchase the selected product (%s)' % product_to_purchase.name
                else:
                    self.player.finance.assets.append(self.market.buy_product(product_to_purchase))
                    self._update_userxp()
            elif user_command == '2':
                self._status_message = ''
                break

    def _assets(self):
        while True:
            self._status_line()
            print('Asset management menu')
            print('---------------------')
            self.player._list_assets()
            user_command = input('1) Sell asset - 2) Exit Asset Management - Make your choice: ')
            if user_command == '1':
                # Todo: add required code.
                # Increase xp when something was sold
                pass
            if user_command == '2':
                break

    def _casino(self):
        # Todo: make gamescreen menu
        self._status_line()
        print('Welcome to Casino Keanu!')
        print('------------------------')
        print('Presently we can offer you the following choices:')
        print('1) Coinflip')
        print('2) Roll dice')
        pass

    def _bank(self):
        while True:
            self._status_line()
            print('Welcome to Bank Keanu')
            print('---------------------')
            user_command = input('1) Request loan - 2) Repay loan - 3) Leave the bank - Your choice: ')
            if user_command == '1':
                self.bank.request_loan()
            elif user_command == '2':
                self.bank.repay_loan()
            elif user_command == '3':
                break

    def _player_turn(self):
        user_command = input('1) The Market - 2) Asset management - 3) The Bank - 4) Game menu - Your choice: ')
        if user_command == '1':
            self._market()
        elif user_command == '2':
            self._assets()
        elif user_command == '3':
            self._bank()
        elif user_command == '4':
            return False
        return True

    def play(self):
        while True:
            self._game_screen()
            if not self._player_turn():             # Execute player's turn
                break                               # or exit game.
            # Check for time-based event
            #   Update player's Finance
            #       Update income
            # Check if newly available assets became available on the Market (unlocked objects) -> Depends on self.player.xp
            self._update_level()                    # Let's check if we reached a new level.
