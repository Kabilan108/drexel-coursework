# CS 171 - Final Question 5 (20.5)
# Purpose: This program retrieves and prints movie infromation from a specified
#          text file.
# Author:  Tony Kabilan Okeke (tko35)
# Date:    03.15.2022

# Imports
import os

# Definitions
def getFileName():
    """
    Prompt user to provide file name, and ensure file exists.
    @return file name
    """
    while True:
        file_name = input("Enter name of the data file: ")
        if os.path.isfile(file_name):
            break
        print("Error: that file does not exist. Try again.")

    return file_name

def movieFinder(inFile, movieTitle):
    """
    Determine whether a specific movie is stored in the inFile
    @param inFile
        a file object that has been opened for reading
    @param movieTitle
        a string that represents the title of the movie to look for.
    @return (bool, int, float)
        a tuple indicating whether movie was found, its running time, and rating
    """

    # Parse file
    lines = inFile.readlines()
    lines = [line.strip().split('\t') for line in lines]

    # Store movie information in a nested dictionary
    movie_info = {
        m: {'Genre': g, 'Year': int(y), 'Runtime': int(rt), 'Rating': float(rat)}
        for (m, g, y, rt, rat) in lines
    }

    # Determine whether movie is in file and return tuple
    if movieTitle in movie_info:
        return (True, movie_info[movieTitle]['Runtime'], movie_info[movieTitle]['Rating'])
    else:
        return (False, 0, 0)

def createReport(inFile, genre):
    """
    Report how many movies of a certain genre are in the data file
    @param inFile
        a file object for a file that has been opened for reading.
    @param genre
        a string that represents a genre.
    @return 
        integer that represents the number of movies of the given genre, found in the data file
    """
    # Parse file
    lines = inFile.readlines()
    lines = [line.strip().split('\t') for line in lines]

    # Count how many movies of a specific genre are found
    num_movies = 0
    movie_titles = []
    for line in lines:
        if line[1] == genre:
            # Count movie
            movie_titles.append(line[0])
            num_movies += 1

    # Store data in output file
    outFile = open("movieReport.txt", 'w')
    outFile.writelines([title+'\n' for title in movie_titles])
    outFile.writelines([f'\nGenre: {genre}\n', f'Total movies: {num_movies}'])
    outFile.close()

    # Return number of movies found
    return num_movies

def main():
    """
    Run program
    """
    # Prompt user for filename
    file_name = getFileName()

    # Prompt user for movie title
    movie_title = input("Enter title of a movie: ").capitalize()

    # Determine whether movie is in file
    inFile = open(file_name, 'r')
    movie_found = movieFinder(inFile, movie_title)  
    inFile.close()

    # Display the running time and rating of the movie if found
    if movie_found[0]:
        print(f"{movie_title} has a running time of {movie_found[1]} minutes and a rating of {movie_found[2]} stars.")
    else:
        print(f"{movie_title} was not found in the file.")

    # Ask the user for a genre and save output of all movies in that genre
    genre = input("What type of movie would you like to watch? ").capitalize()
    inFile = open(file_name, 'r')
    num_movies = createReport(inFile, genre)
    inFile.close()
    print(f"Genre: {genre}\nMovies Found: {num_movies}")


if __name__ == "__main__":
    main()