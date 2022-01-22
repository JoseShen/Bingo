import sys 
from sys import exit
import random
import os

def validate_seed(file):
    with open(file, 'r') as file_open:
        # Checking seed
        contents = file_open.readlines()
        seed = contents.pop(0)[:-1] # Grabs the seed removes \n

        if len(seed) != 4:
            print("Invalid seed: Invalid seed length")
        else:
            for c in range(len(seed)):
                if not seed[c].isdigit():
                    print("Invalid seed") 
                    sys.exit(1)

def validate_card(file):
    with open(file, 'r') as file_open:
        # Checking card format
        number_lines = file_open.readlines()[1:] 
        new_list = []
        for line in number_lines:
            new_list.append(line.strip()) 

        for line in new_list:
            if len(line) != 14:
                print("Invalid Card Format")
                sys.exit(1)

        TwoD_Array = []
        for numbers in new_list:
            TwoD_Array.append(numbers.split(' '))
        # Validating each number
        if TwoD_Array[2][2] != '00':
            print("Card Format Error: Missing 00")
            sys.exit(1)
        for row in range(len(TwoD_Array)):
            for column in range(len(TwoD_Array[row])):
                if column == 0:
                    if TwoD_Array[row][column][0] == '0':
                        number = int(TwoD_Array[row][column][1:])
                        if number < 0 or number > 15:
                            print("Card Format Error: Column 0")
                            sys.exit(1)
                    else:
                        number = number = int(TwoD_Array[row][column])
                        if number < 0 or number > 15:
                            print("Card Format Error: Column 0")
                            sys.exit(1)
                elif column == 1:
                    number = int(TwoD_Array[row][column])
                    if number < 16 or number > 30:
                        print("Card Format Error: Column 1")
                        sys.exit(1)
                elif column == 2:
                    if row != 2 and column !=2: 
                        number = int(TwoD_Array[row][column])
                        if number < 31 or number > 45:
                            print("Card Format Error: Column 2")
                            sys.exit(1)
                    elif row != 2:
                        number = int(TwoD_Array[row][column])
                        if number < 31 or number > 45:
                            print("Card Format Error: Column 2")
                            sys.exit(1)
                elif column == 3:
                    number = int(TwoD_Array[row][column])
                    if number < 46 or number > 60:
                        print("Card Format Error: Column 3")
                        sys.exit(1)
                elif column == 4:
                    number = int(TwoD_Array[row][column])
                    if number < 61 or number > 75:
                        print("Card Format Error: Column 4")
                        sys.exit(1)


def get_seed(file):
    with open(file, 'r') as file_open:
        contents = file_open.readlines()
        seed = int(contents.pop(0)[:-1])
    return seed



def get_array(file):
    with open(file, 'r') as file_open:
    # Checking card format
        number_lines = file_open.readlines()[1:] 
        new_list = []
        for line in number_lines:
            new_list.append(line.strip())
        TwoD_Array = []
        for numbers in new_list:
            TwoD_Array.append(numbers.split(' ')) 
    return TwoD_Array

def check_array(array, number):
    array[2][2] = '00m'
    for row in range(len(array)):
        for column in range(len(array[row])):
            if array[row][column][0] == '0' and array[row][column][1] == str(number):
                array[row][column] = array[row][column] + "m"
            if array[row][column] == str(number):
                array[row][column] = str(number) + 'm'
    return array

def print_array(array): 
    for row in range(len(array)):
        for column in range(len(array[row])):
            print('{:<3}'.format(array[row][column]), end= " ")
        print()

def win(array):
    corner1 = array[0][0][-1]
    corner2 = array[0][4][-1] 
    corner3 = array[4][0][-1]
    corner4 = array[4][4][-1]
    if corner1 == 'm' and corner2 == 'm' and corner3 == 'm' and corner4 == 'm':
        print("Winner by 4 corners")
        sys.exit(1)
    for row in range(len(array)):
        win_row = 0
        for column in range(len(array[row])):
            if array[row][column][-1] == 'm':
                win_row += 1
        if win_row == 5:
            print("Winner by row")
            sys.exit(1)
    for column in range(len(array)):
        win_column = 0
        for row in range(len(array[column])):
            if array[row][column][-1] == 'm':
                win_column += 1
        if win_column == 5:
            print("Winner by column")
            sys.exit(1)


def call_list_letter(number):
    if number > 0 and number <= 15:
        number = str(number) + "L"
    elif number >= 16 and number <= 30:
        number = str(number) + "I"
    elif number >= 31 and number <= 45:
        number = str(number) + "N"
    elif number >= 46 and number <= 60:
        number = str(number) + "U"
    elif number >= 61 and number <= 75:
        number = str(number) + "X"
    return number

def print_array_first_time(array):
    array[2][2] = '00m'
    for row in range(len(array)):
        for column in range(len(array[row])):
            print('{:<3}'.format(array[row][column]), end= " ")
        print()
def LINUX():
    s = "LINUX"
    for i in s:
        print(" {:<3}".format(i), end = "")
    print()


def game_loop(file):
    call_list = []
    numbers = []
    validate_seed(file)
    seed = get_seed(file)
    random.seed(seed)
    validate_card(file)
    random.seed(seed)
    array = get_array(file)
    letter = ''
    first = True
    while letter != 'q':
        if first:
            print("Call list: ")
            print()
            LINUX()
            print_array_first_time(array)
            first = False
        elif first == False:
            number = random.randint(1, 75)
            if number not in numbers:
                numbers.append(number)
                checked = check_array(array, number)
                call_list.append(call_list_letter(number))
            print("Call list: ", end="")
            print(" ".join(call_list))
            print()
            LINUX()
            print_array(checked)
            win(checked)
        letter = input("Enter a letter: ")
        os.system('cls')
        if letter == 'q':
            sys.exit(1)


if __name__ == '__main__':
    file = sys.argv[1]
    game_loop(file)






    