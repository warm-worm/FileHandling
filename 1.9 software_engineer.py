###
# Prints employees employed in a specified position.
#

# Employee List
file_name = 'it_company.csv'

# Position
job_title = 'Software Engineer'

with open(file_name, 'r') as file:
   for i, line in enumerate(file , 1):
      if job_title in line:         #strip() instead of end=""
         formatted_line = line.strip().replace(',' , ', ') #added spaces after commas
         print(f'{i}. {formatted_line}')
