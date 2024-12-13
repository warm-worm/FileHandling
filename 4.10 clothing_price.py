##
# The clothing.csv contains a list of clothing in stock. Write a program that prints 
# those products whose price is less than 60 and whose stock is less than 40.
##
import csv

def filter_clothes(file_name):
    try:
        with open(file_name, 'r') as file:
            reader = csv.DictReader(file) # each column accessed by its name
            for row in reader:
                price = float(row['Price']) # price to float for comparison
                stock = int(row['Stock_Quantity']) # to int for comparison
                if price < 60 and stock < 40:
                    print(f"Product: {row['Product_Name']}, Price: {row['Price']}, Stock: {row['Stock_Quantity']}")
    except FileNotFoundError:
        print(f"The file {file_name} doesn't exist.")

filter_clothes('clothing.csv')
