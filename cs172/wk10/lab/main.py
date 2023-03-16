# File Name: main.py
# Purpose:   Main script for Lab 9
# Author:    Tony Kabilan Okeke <tko35@drexel.edu>
# Date:      March 16, 2023


from birthday import Birthday


def main():
    """Main Function"""

    # Get path to file
    while True:
        try:
            path = input("Enter name of the data file: ")
            with open(path, "r") as f:
                break
        except FileNotFoundError:
            print("Error: that file does not exist. Try again.")
    print()

    # Create an empty hash table
    hash_table = [[] for _ in range(12)]

    # Read birthdays from file and create Birthday objects
    with open(path, "r") as f:
        for bday in f.readlines():
            month, day, year = bday.strip().split("/")
            birthday = Birthday(int(month), int(day), int(year))
            hash_table[hash(birthday)].append((birthday, f.tell()))

    # Output the total length of the list at each of the hash locations
    for i, bday_list in enumerate(hash_table):
        print(f"Hash location {i} has {len(bday_list)} elements in it")


if __name__ == "__main__":
    main()

