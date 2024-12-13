###
# Checks the correctness of username and password
#
import re

# read username and password from keyboard
username = input('Enter the username: ')
password = input('Enter the password: ')

# pattern (criteria) for username and password $ -> pattern applies to the whole string
username_pattern = r'^[a-z]{6,}$' # must only be lowercase and be at least 6 characters long
password_pattern = r'^[A-Za-z0-9_]{8,}$' # only contains letters, numbers and _

# check if username and password are ok
username_match = re.match(username_pattern,username)
password_match = re.match(password_pattern,password)

# print results
if username_match and password_match:
   print('The username and the password are both correct.')
else:
   print('The username and/or password are/is incorrect.')