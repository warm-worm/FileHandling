##
# Program that calculates the number of lines, characters and words for any text file
# The user enters the name of the file from the keyboard. Use a try-except block to avoid 
# interrupting your program when the user enters a filename that doesn't exist. Print the 
# result of the calculation. To check if the program is working correctly, find 3 text files
# on the Internet and use them to test the program.
##

def calculate_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)
            num_char = sum(len(line) for line in lines)
            num_words = sum(len(line.split()) for line in lines)
        print(f'File name: {file_name}')
        print(f'Number of lines: {num_lines}')
        print(f'Number of characters: {num_char}')
        print(f'Number of words: {num_words}')

    except FileNotFoundError:
        print(f"The file {file_name} doesn't exist.")

filename = input('Enter the name of the file: ')
calculate_file(filename)
