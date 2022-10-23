"""
Authors: [Tony Kabilan Okeke](mailto:tko35@drexel.edu),
         [Cooper Molloy](mailto:cdm348@drexel.edu)

This function will:
- Create the table 'names' if it does not already exist; the table will
  have two fields: 'id' and 'name'
  - Assume the name will be at most 16 characters long
- Insert the given name into the table
- Return the number of names in the table
"""

import sqlite3

def db_insertname(dbfile: str, name: str) -> int:

    # Connect to the database
    db = sqlite3.connect(dbfile)

    # Create the table if it doesn't exist
    db.execute("""
    CREATE TABLE IF NOT EXISTS names (
        id INTEGER PRIMARY KEY,
        name TEXT(16)
    );
    """)

    # Insert the name
    db.execute("INSERT INTO names (name) VALUES (?)", (name,))
    db.commit()

    # Get the number of names in the table
    count = db.execute("SELECT COUNT(*) FROM names").fetchone()[0]

    # Close the database
    db.close()

    return count
