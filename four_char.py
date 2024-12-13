##
# The files.txt contains a list of file names. Write a program that prints only those file 
# names whose extensions consist of exactly four characters (e.g. .html)
##

def files_extentions(file_name):
    try:
        with open(file_name, 'r') as file:
            for line in file:
                line = line.strip()
                if '.' in line:
                    extention = line.split('.')[-1] # the part after the dot
                    if len(extention) == 4:
                        print(line)
    except FileNotFoundError:
        print(f"The file {file_name} doesn't exist.")

files_extentions('files.txt')