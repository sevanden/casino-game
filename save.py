"""
THIS IS A CUSTOM MODULE TO SAVE FILES AND DATA
THIS CAN BE USED IN GAMES, TEXT PROGRAMS AND MUCH
MORE MADE IN PYTHON
TYPE 'import save' TO IMPORT IT INTO YOUR PROGRAM
AND THEN TYPE 'save.save_data[<list of date>, <file name without extension>, <mode>]'
"""
def save_data(datalist, filename, save_mode):
    save_file = open("save/" + filename + ".dat", mode=save_mode)
    for data in datalist:
        save_file.writelines(data + "\n")
    save_file.close()

def create_file(filename):
    try:
        save_file = open("save/" + filename + ".dat", mode="r")
        save_file.close()
        invalid_option = True
        while invalid_option:
            option = raw_input("\nSave file already exists, do you want to replace it? (y/n)> ")
            print("\n")
            if option == "y":
                invalid_option = False
                save_file = open("save/" + filename + ".dat", mode="w")
                save_file.close()
                return False
            elif option == "n":
                invalid_option = False
                return True
            else:
                print("You didn't enter a valid option!")
    except IOError:
        save_file = open("save/" + filename + ".dat", mode="w")
        save_file.close
        return False
#in development and stuff blabla 