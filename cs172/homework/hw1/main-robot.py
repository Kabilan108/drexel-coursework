# File Name:   main-robot.py
# Purpose:     Main routine to create and run the robot
# Author:      Tony Kabilan Okeke
# Date:        January 16, 2023

# Import the robot class
from robot import Robot

# Functions for input validation
def prompt(message: str, error: str, valid: list, dtype: str) -> float:
    """
    Prompt the user for a number within a range
    
    Parameters
    ----------
    message : str
        The initial input prompt
    error : str
        The prompt to use if first attempt raises and error
    valid : list
        The lower and upper limits of acceptable values
    dtype : str
        What type of number is desired, either 'int' or 'float'
    """

    while True:
        try:
            if dtype == 'float':
                value = float(input(message))
            elif dtype == 'integer':
                value = int(input(message))
            else:
                raise Exception("dtype must be either 'float' or 'int'")
                break

            if valid[0] <= value <= valid[1]:
                return value
            else:
                print("Error: you entered a value out of range. Try again.")
                message = error
        except ValueError:
            message = f"Invalid input: an {dtype} value was expected. Try again: "
            continue


# Main routine
if __name__ == "__main__":
    # Prompt for battery level
    level = prompt(
        "Enter the robot's current battery's level (a value between 0 and 10.00): ",
        "Enter a value between 0.0 and 10.0: ",
        [0, 10],
        "float"
    )

    # Create a robot
    robot = Robot(level)

    # Display current battery level and speed
    print(
        f"\nRobot's current battery level: {robot.getBatteryLevel():.2f}\n"
        f"Robot's current speed: {robot.getCurrentSpeed():.2f}\n"
    )

    # Prompt for distance to move
    distance = prompt(
        "Enter the distance to move forward (a value between 0 and 20): ",
        "Enter a value between 0 and 20: ",
        [0, 20],
        "integer"
    )

    # Move the robot
    robot.moveForward(distance);

    # Display robot information
    print(
        f"\nRobot's current battery level: {robot.getBatteryLevel():.2f}\n"
        f"Robot's distance traveled: {robot.getDistanceTraveled():d}\n"
        f"Robot's current speed: {robot.getCurrentSpeed():.2f}\n"
        f"Time needed to go back to base: {robot.getEstimatedTimeHome():.2f}\n\n"
    )

    # Prompt for charging battery
    amount = prompt(
        "Enter the amount to charge Robot's battery (a value between 0 and 10.00): ",
        "Enter a value between 0.0 and 10.0: ",
        [0, 10],
        "float"
    )

    # Charge the battery
    robot.charge(amount)

    # Display robot information
    print(
        f"\nAfter recharging the battery:\n"
        f"Robot's current battery level: {robot.getBatteryLevel():.2f}\n"
        f"Robot's current speed: {robot.getCurrentSpeed():.2f}\n"
        f"Time needed to go back to base: {robot.getEstimatedTimeHome():.2f}"
    )

