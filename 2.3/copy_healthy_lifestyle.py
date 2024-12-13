###
# Makes a copy of a text file
#

# file names
original_file = 'healthy_lifestyle.txt'
target_file = 'copy_healthy_lifestyle.txt'

# read the content of the original file
with open('healthy_lifestyle.txt', 'r') as file:
   content = file.read()

# write the content to the target file (copy)
with open('copy_healthy_lifestyle.txt', 'w') as file:
   content = file.write(content)
