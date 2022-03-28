# CS 171 - Homework 6 (Can you drive safely?)
# Purpose: Display an Impairment Chart showing Blood Alcohol Concentration
#          values for an individual with a specified weight and sex, 
#          based on how much time has passed since their last drink.
# Author:  Tony Kabilan Okeke (tko35)
# Date:    02.19.2022

# Function definitions
def computeBloodAlcoholConcentration(drinks, weight, duration):
    """
    Computes the blood alcohol concentration (BAC) based on
    the number of drinks, weight, and duration.
    @param drinks
        number of drinks consumed
    @param weight
        the weight of the individual
    @param duration
        the time (in minutes) since last drink was consumed
    @return 
        tuple with male and female bac values
    """
    # Compute male and female BAC (Only account for time if drinks > 0)
    bac_f = 4.5*(drinks / weight) - 0.01*(duration / 40)*(drinks > 0)
    bac_m = 3.8*(drinks / weight) - 0.01*(duration / 40)*(drinks > 0)

    return (bac_m, bac_f)

def impairment(bac):
    """
    Returns a string with an appropriate message for the blood
    alcohol concentration.
    @param bac
        A blood alcohol concentration value
    @return 
        string with appropriate message for bac
    """
    if bac == 0.0:
        return "Safe to Drive"
    elif bac <= 0.04:
        return "Some Impairment"
    elif bac <= 0.08:
        return "Driving Skills Significantly Affected"
    elif bac <= 0.10:
        return "Criminal Penalties in Most US States"
    elif bac <= 0.30:
        return "Legally Intoxicated - Criminal Penalties in All US States"
    else:
        return "Death is Possible!"

def showImpairmentChart(weight, duration, sex):
    """
    Prints an impairment chart based on the provided weight and sex.
    @param weight
        the weight of the individual
    @param duration
        the time (in minutes) since last drink was consumed
    @param sex
        sex of the individual ('m' or 'f')
    @return None
    """
    # Create index for bac tuple based on provided sex
    bac_ind = 0 if sex == 'm' else 1

    # Write sex in full
    sex = 'male' if sex == 'm' else 'female'
    
    # Print Table header
    print( f"\n{weight} pounds, {sex}, {duration} minute(s) since last drink" )
    print( f"#drinks{' '*3}BAC{' '*7}Status" )

    # Compute bac values
    bacs = [ computeBloodAlcoholConcentration(d, weight, duration) for d in range(12) ]

    # Print table
    for (i, bac) in enumerate(bacs):
        print( f"{i:<10d}{bac[bac_ind]:<10.4f}{impairment(bac[bac_ind])}" )
    
    return

def promptForInteger(lower, upper):
    """
    Validate user input, ensuring only integer values in a specific range are provided.
    @param lower
        lower bound for integer (inclusive)
    @param upper
        upper bound for integer (inclusive)
    @return integer
    """
    while True:
        try:
            value = int( input() )
            if lower <= value <= upper:
                break
            else:
                print("Error: value out of bounds")
        except:
            print("Error: An integer value was expected. Try again")
    
    return value

def promptForMorF():
    """
    Repeatedly ask user for a character until they enter 'M' or 'F' (case insensitive)
    @return string ('m' or 'f')
    """
    while True:
        value = input()
        if value.lower() in ['m', 'f']:
            break
        else:
            print("Error: you must enter M or F")

    return value.lower()

def main():
    """
    Run program.
    """
    # Gather Input
    print("Enter your weight (in lbs):")
    weight = promptForInteger(0, 500)
    print("How many minutes has it been since your last drink?")
    duration = promptForInteger(0, 300)
    print("Enter your sex as M or F:")
    sex = promptForMorF()

    # Print impairment table
    showImpairmentChart(weight, duration, sex);

if __name__ == '__main__':
    main()