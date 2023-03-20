# CS 172 - Final Exam
# Purpose: Main application
# Author:  Tony Kabilan Okeke (tko35)
# Date:    03.20.2023

from solids import Sphere, Cone
from solidset import SolidSet


def displayMenu():
    """Print a menu"""
    opts = [
        "Display all the solid shapes in the solid set.",
        "Search for and display a certain solid by its ID.",
        "Display all the spheres in the solid set.",
        "Display all the cones in the solid set.",
        "Add a sphere to the solid set.",
        "Add a cone to the solid set.",
        "Get the total volume of the solid set.",
        "Quit the application.",
    ]

    print("Welcome to solid set!")
    print("Enter one of the following numbers for options:")
    for i, opt in enumerate(opts, 1):
        print(f"{i}. {opt}")
    print()


if __name__ == "__main__":
    # Instantiate the SolidSet
    SS = SolidSet()

    # Main loop
    while True:
        # Show menu
        displayMenu()

        # Let user choose
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice. Try again.")
            continue

        if choice == 1:
            # Show list of solids
            for solid in SS.getSolids():
                print(solid)
                print()
            print()

        elif choice == 2:
            # Find a specified solid in the SolidSet
            try:
                ID = int(input("Enter a solid ID: "))
            except ValueError:
                print("Invalid ID. Try again.")
                continue

            found = False
            for solid in SS.getSolids():
                if solid.getID() == ID:
                    found = True
                    break
            if found:
                print(f"Found ID: {ID}")
                print(solid)
                print()
            else:
                print(f"Cannot Find ID: {ID}\n")

        elif choice == 3:
            # List all Spheres
            for solid in SS.getSpheres():
                print(solid)
                print()
            print()

        elif choice == 4:
            # List all Cones
            for solid in SS.getCones():
                print(solid)
                print()
            print()

        elif choice == 5:
            # Add a Sphere
            try:
                radius = float(input("Enter the radius: "))
                color = input("Enter color: ")
            except ValueError:
                print("Invalid value. Try again.")
                continue

            solid = Sphere(radius, color)
            SS.addSolid(solid)

        elif choice == 6:
            # Add a Cone
            try:
                radius = float(input("Enter the radius: "))
                height = float(input("Enter the height: "))
                color = input("Enter color: ")
            except ValueError:
                print("Invalid value. Try again.")
                continue

            solid = Cone(radius, height, color)
            SS.addSolid(solid)

        elif choice == 7:
            # Calculate total volume
            print(f"Total Volume of Solid Set is: {SS.getTotalVolume()}\n")

        elif choice == 8:
            print("Goodbye")
            break

        else:
            print("Invalid choice. Try again.\n")
