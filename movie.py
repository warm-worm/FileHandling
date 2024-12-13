# Program to write movie details to a text file

# Variables containing movie details
movie_title = "Inception"
director = "Christopher Nolan"
lead_actor = "Leonardo DiCaprio"

# Name of the file to write to
file_name = 'movie_details.txt'

# Writing movie details to the file
with open(file_name, 'w') as file:
   file.write(f"Movie Title: {movie_title}\n") # \n means to move the cursor to the next line
   file.write(f"Director: {director}\n")
   file.write(f"Lead Actor: {lead_actor}\n")

print(f"Movie details have been written to {file_name}.")

# Variables: movie_title, director, and lead_actor hold the details of the movie.
# Opening the file: with open(file_name, 'w') opens the file in write mode ('w'), creating or overwriting the file.
# Writing details: Uses the write() method to write each movie detail to the file, adding \n at the end of each line for formatting (move to next line).
# Automatic file closing: The 'with' statement ensures the file is properly closed after writing.