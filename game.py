# coding=utf-8

import pickle
from game_keanu import Game
import time
import os


def main_menu():
    os.system('clear')
    print('Main menu')
    print('---------')
    print('Welcome to my new casino and money building game!')
    print('Here you can gamble without losing any real money.')
    print('--------------------------------------------------')
    print('1) runs the game')
    print('2) opens readme')
    print('3) makes a backup of a chosen save file')
    print('4) removes a chosen backup file')
    print('5) moves a chosen backup file into save folder')
    print('6) exits the program')


def game_menu():
    os.system('clear')
    print('Game menu')
    print('---------')
    print('All you lose here is time, have fun!')
    print('1) New game')
    print('2) Load game')
    print('3) Save game')
    print('4) Resume to game')
    print('5) Exit game')


def display_readme():
    readme = open('README.md', mode='r')
    lines = readme.read().split('\n')
    print('\n' * 5)
    for line in lines:
        print
        line
    readme.close
    time.sleep(120)


def backup_savedgame():
    # Todo: review if code is really required
    file_to_backup = input('Enter the filename (without .dat) that you want to backup>>> ')
    try:
        os.system('cp save/' + file_to_backup + '.dat backup_save/' + file_to_backup + '.dat')
    except:
        print('Something went wrong backing up the file!')


def delete_savedgame():
    # Todo: review if code is really required
    file_to_remove = input('Enter the filename (without .dat) that you want to remove from the backup folder>>> ')
    confirm = input('Are you sure you want to delete ' + file_to_remove + '.dat (y/n)? >>> ')
    if confirm == 'y':
        os.system('rm backup_save/' + file_to_remove + '.dat')


def move_savedgame():
    # Todo: review if code is really required
    file_to_move = input('Enter the filename (without .dat) you want to move to the save folder>>> ')
    confirm = input('Are you sure you want to move '
                    + file_to_move +
                    '.dat, if the filename already exists in the save folder it will be over written (y/n)? >>> ')
    if confirm == 'y':
        os.system('cp backup_save/' + file_to_move + '.dat save/' + file_to_move + '.dat')


def main():
    while True:
        main_menu()
        main_option = input('Chose your option: ')
        if main_option == '1':
            while True:
                game_menu()
                option = input('Chose your option: ')
                if option == '1':
                    player_name = input('What is your name? ')
                    difficulty = input('Chose your difficulty level (1-2-3): ')
                    my_game = Game(player_name, difficulty)
                    my_game.play()
                elif option == '2':
                    # Todo: add version to saved game to ensure future loads are compatible.
                    game_file = open('data/save/%s.dat' % str(input('Enter the name of the saved game file without extension: ')), 'br')
                    my_game = pickle.load(game_file)
                    my_game.play()
                elif option == '3':
                    my_game.save()
                elif option == '4':
                    try:
                        my_game.play()                                                                                  # Resume game
                    except UnboundLocalError:
                        print('You have not yet launched or loaded a game.')                                            # This will not be visible to the user.
                    else:
                        pass
                elif option == '5':
                    break
        elif main_option == '2':
            display_readme()
        elif main_option == '3':
            backup_savedgame()
        elif main_option == '4':
            delete_savedgame()
        elif main_option == '5':
            move_savedgame()
        elif main_option == '6':
            break


if __name__ == '__main__':
    main()