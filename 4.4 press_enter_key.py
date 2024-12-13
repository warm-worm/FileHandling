##
# Program that displays the first five lines from the it_company.csv file and then prints 
# 'Press Enter key...' in the next line and waits for the Enter key to be pressed. 
# The program repeats printing the next five lines from the file, waiting for the Enter key 
# to be pressed each time.
##

file_name = 'it_company.csv'

def display_lines(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines() # to read all lines into a list

        line_number = 0 # starting number

        while line_number < len(lines): # loops until all lines displayed
            for i in range(line_number, min(line_number + 5, len(lines))):
                print(lines[i], end='')
            line_number += 5
            input('\nPress Enter key to continue...')

display_lines(file_name)

