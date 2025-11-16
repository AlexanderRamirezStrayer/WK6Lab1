# This program manages a list of movie titles stored in a text file (movies.txt).

import os

# --- Global Constants ---
FILE_NAME = "movies.txt"
WIDTH = 55
SEPARATOR = "=" * WIDTH

# --- Part 1: File Initialization ---

def initialize_file(file_name):
    """
    Creates the file and writes the initial three movie titles.
    """
    try:
        if not os.path.exists(file_name):
            initial_titles = [
                "Cat on a Hot Tin Roof",
                "On the Waterfront",
                "Monty Python and the Holy Grail"
            ]
            # Open the file in write mode ('w') to create/overwrite and save initial titles
            with open(file_name, "w") as file:
                for title in initial_titles:
                    file.write(title + "\n")
            print(f"\nSUCCESS: Created '{file_name}' and added initial titles.")
        else:
            print(f"\nNote: '{file_name}' already exists. Using existing file data.")
    except IOError:
        print(f"\nFATAL ERROR: Could not create or write to file '{file_name}'.")

# --- Part 2: Display Heading and Menu ---

def display_menu():
    """
    Displays the program heading and the menu options.
    """
    print("\n" + SEPARATOR)
    print("           FILE-BASED MOVIE LIST MANAGER")
    print(SEPARATOR)
    print("Please choose a command from the list below:")
    print("  1. Display Movies")
    print("  2. Add Movie")
    print("  3. Delete Movie")
    print("  4. Exit Program")
    print(SEPARATOR)

# --- Part 3: Load Data from File ---

def read_titles(file_name):
    """
    Opens the file and populates a list with all movie titles.
    
    Returns:
        list: The list of movie titles.
    """
    movie_list = []
    try:
        # Open the file in read mode ('r')
        with open(file_name, "r") as file:
            for line in file:
                # Use .strip() to remove leading/trailing whitespace, including newline characters
                movie_list.append(line.strip())
        return movie_list
    except FileNotFoundError:
        print(f"ERROR: File '{file_name}' not found. Initializing empty list.")
        return []
    except IOError:
        print(f"ERROR: Could not read file '{file_name}'. Returning empty list.")
        return []

# --- Helper Function for File Writing ---

def write_titles(file_name, movie_list):
    """
    Writes all current titles in the list back to the file (overwriting the old content).
    """
    try:
        # Open the file in write mode ('w') to overwrite content
        with open(file_name, "w") as file:
            for title in movie_list:
                file.write(title + "\n")
    except IOError:
        print(f"\nFATAL ERROR: Could not write data to file '{file_name}'. Changes may be lost.")

# --- Part 4: Menu Functionality ---

def display_list(movie_list):
    """
    Displays all movie titles in the list with their corresponding index number.
    """
    print(SEPARATOR)
    if not movie_list:
        print("The movie list is currently empty.")
        print(SEPARATOR)
        return

    print("CURRENT MOVIE LIST:")
    print("-" * WIDTH)
    for i, title in enumerate(movie_list, 1):
        print(f"{i}. {title}")
    print(SEPARATOR)


def add_title(movie_list, file_name):
    """
    Prompts for a title, adds it to the list, writes the list to the file, and displays the list.
    """
    new_title = input("\nEnter the title of the movie to add: ").strip()
    if new_title:
        movie_list.append(new_title)
        
        # Write the values in the list back to the file movies.txt
        write_titles(file_name, movie_list)
        print(f"\nSUCCESS: '{new_title}' was added and saved to file.")
    else:
        print("\nERROR: Movie title cannot be empty.")
    
    # Call the function to display all the titles in the list
    display_list(movie_list)


def delete_title(movie_list, file_name):
    """
    Prompts for a number, deletes the title, writes the list to the file, and displays the list.
    """
    # Show the list first so the user knows which number to enter
    display_list(movie_list)

    if not movie_list:
        print("Nothing to delete.")
        return

    try:
        # User enters the number corresponding to the title (1-based index)
        index_to_delete = int(input("Enter the number of the movie to delete: "))
        
        # Convert user's 1-based index to Python's 0-based index
        zero_based_index = index_to_delete - 1 

        # Check for invalid number (out of range)
        if 0 <= zero_based_index < len(movie_list):
            deleted_title = movie_list.pop(zero_based_index)
            
            # Write the values in the list back to the file movies.txt
            write_titles(file_name, movie_list)
            print(f"\nSUCCESS: '{deleted_title}' was deleted and changes were saved to file.")
        else:
            # If the user enters an invalid number display a message
            print(f"\nERROR: Invalid number entered. Please enter a number between 1 and {len(movie_list)}.")
            
    except ValueError:
        # If the user enters non-integer input
        print("\nERROR: Invalid input. Please enter a whole number.")
    
    # Call the function to display all the titles in the list
    display_list(movie_list)

# --- Main Program Execution ---

def main():
    """
    Handles file initialization, loads data, and runs the main menu loop.
    """
    # Part 1: Create/Initialize the text file
    initialize_file(FILE_NAME)
    
    # Part 3: Load movie titles from file into the list
    movie_list = read_titles(FILE_NAME)
    
    # Start the loop
    while True:
        
        # Part 2: Display heading and menu
        display_menu()
        
        command = input("Command: ").strip()
        
        if command == '1':
            # Call function to display all the titles
            display_list(movie_list)
        
        elif command == '2':
            # Call function to add a title (handles file writing and display)
            add_title(movie_list, FILE_NAME)
            
        elif command == '3':
            # Call function to delete a title (handles file writing and display)
            delete_title(movie_list, FILE_NAME)
            
        elif command == '4':
            # Exit the program
            print(SEPARATOR)
            print("Exiting program. All changes saved. Goodbye!")
            print(SEPARATOR)
            break
            
        else:
            # If the user entered an invalid command display a message
            print(SEPARATOR)
            print(f"ERROR: Invalid command '{command}'. Please choose 1, 2, 3, or 4.")
            print(SEPARATOR)

if __name__ == "__main__":
    main()