import time
import os

exit = False
print("Welcome to my new casino and money building game!\n")
while not exit:
    print("""
1)      runs the game
2)      opens readme
3)      makes a backup of a chosen save file
4)      removes a chosen backup file
5)      moves a chosen backup file into save folder
0)      exits the program""")

    option = raw_input(">>> ")
    if option == "1":
        import game
    elif option == "2":
        readme = open("README.md", mode="r")
        lines = readme.read().split("\n")
        print("\n" * 5)
        for line in lines:
            print line
        readme.close
        time.sleep(120)
    elif option == "3":
        file_to_backup = raw_input("Enter the filename (without .dat) that you want to backup>>> ")
        try:
            os.system("cp save/" + file_to_backup + ".dat backup_save/" + file_to_backup + ".dat")
        except:
            print("Something went wrong backing up the file!")
    elif option == "4":
        file_to_remove = raw_input("Enter the filename (without .dat) that you want to remove from the backup folder>>> ")
        confirm = raw_input("Are you sure you want to delete " + file_to_remove + ".dat (y/n)? >>> ")
        if confirm == "y":
            os.system("rm backup_save/" + file_to_remove + ".dat")
    elif option == "5":
        file_to_move = raw_input("Enter the filename (without .dat) you want to move to the save folder>>> ")
        confirm = raw_input("Are you sure you want to move " + file_to_move + ".dat, if the filename already exists in the save folder it will be over written (y/n)? >>> ")
        if confirm == "y":
            os.system("cp backup_save/" + file_to_move + ".dat save/" + file_to_move + ".dat")
    elif option == "0":
        exit = True
