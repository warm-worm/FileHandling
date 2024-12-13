##
# Write a program that calculates, prints, and saves to a text file integers from 1 to 100 
# and their second and third powers. Sample result:
# 1,1,1
# 2,4,8
# 3,9,27
# ...
# ...
##

with open('powers.txt' , 'w') as file:
    for nr in range(1, 101):
        file.write(f'{nr},{nr**2},{nr**3}\n')
        print(f'{nr},{nr**2},{nr**3}')
