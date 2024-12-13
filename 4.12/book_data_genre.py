##
# The file books.csv contains a list of books. Write a program that copies the book data 
# from a given genre to its corresponding file. Use functions to divide the program into 
# logical parts.
# Genre --> Filename
# Fantasy --> books_fantasy.txt
# Historical --> books_historical.txt
# Romance --> books_romance.txt
# Classic --> books_classic.txt  
##
import csv

def filter_by_genre(input_file, genre, output_file):
    with open(input_file, 'r') as file:
        reader = csv.DictReader(file) # to read the file as a dictionary (keys are column names)
        with open(output_file, 'w') as out_file:
            out_file.write('Title, Author, Genre, Year\n') # header
            for row in reader:
                if row['Genre'] == genre: # if genre of the current book matches the given genre
                    out_file.write(f"{row['Title']}, {row['Author']}, {row['Genre']}, {row['Year']}\n")

def process_genres(input_file): # processes genres and their outputs
    genres_and_files = {
        'Fantasy': 'books_fantasy.txt',
        'Historical': 'books_historical.txt',
        'Romance': 'books_romance.txt',
        'Classic': 'books_classic.txt'
    }

    for genre, output_file in genres_and_files.items(): # loops through each genre and processes
        filter_by_genre(input_file, genre, output_file)
        print(f'Books from the genre {genre} genre have been copied to {output_file}.')

input_file = 'books.csv'
process_genres(input_file)
