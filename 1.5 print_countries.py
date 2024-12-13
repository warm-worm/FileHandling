###
# Reads from file, line by line
#
with open('countries.txt', 'r') as file:
    for i, line in enumerate(file , 1):
        print(f'{i}, {line}', end="") # end=""due to the existence of end-of-line characters at the end of lines in the text file
