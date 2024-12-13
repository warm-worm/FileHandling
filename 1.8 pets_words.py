##
# Program that prints the text and counts the number of words in the text
##

def read_from_file(name):
   with open(name, 'r') as file:
      content = file.read()
   return content

file_content = read_from_file('pets.txt')
file_lines = file_content.splitlines()

split_text = file_content.split()
length_text = len(split_text)

print('The amount of words in the text is:', length_text)
