##
# Convenient processing of CSV documents is possible using the CSV module. Find on the 
# Internet how to use this module. Then write a program that, based on the it_company.csv 
# file, prints the first name, last name and email (in the given order, without Job Title) 
# of people employed in the position of 'Graphic Designer'. Sample result:
# GRAPHIC DESIGNERS
# =================
# Chris Martin,chris.martin@example.com
# Jane Taylor,jane.taylor@example.com
# ...
# ...
##
import csv

def print_gd(file_name):
    try:
        with open(file_name, 'r') as file:
            reader = csv.DictReader(file) # to access columns by name
            print('GRAPHIC DESIGNERS')
            print('=================')
            for row in reader:
                if row['Job Title'] == 'Graphic Designer':
                    print(f"{row['First Name']} {row['Last Name']}, {row['Email']}")
    except FileNotFoundError:
        print(f"The file {file_name} doesn't exist.")

print_gd('it_company.csv')
