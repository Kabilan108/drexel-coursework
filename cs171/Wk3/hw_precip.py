# CS 171 - Homework 3 (Precipitation Stats)
# Purpose: This program returns the total annual and monthly precipitation, and months with
#          maximum and minimum precipitation given the precipitation for each month of 
#          the year.
# Author:  Tony Kabilan Okeke (tko35)
# Date:    01.27.2022

# Create a list of the 12 months
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
          'September', 'October', 'November', 'December']

# Define Functions
def getMonthlyPrecip():
  """
  This function prompts the user to provide the precipitation for
  each month of the year.
  """

  # Use list comprehension to collect user input
  precip = [ input( f'Enter total precipitation for {month}: ' ) for month in months ]
  
  # Convert elements of precip to float
  precip = [ float(x) for x in precip ]

  return precip

if __name__ == '__main__':
  # Get monthly precipitation
  precip = getMonthlyPrecip()

  # Computations:
  tot_precip = sum(precip) # Total precipitation
  avg_precip = tot_precip / len(precip) # Average precipitation
  
  # Determine month with highest precipitation
  max_month = precip.index( max(precip) )
  max_precip = ( months[max_precip], precip[max_precip] )
  
  # Determine month with least precipitation
  min_month = precip.index( min(precip) )
  min_precip = ( months[min_precip], precip[min_precip] )

  # Print results
  print( f"\nTotal precipitation: {tot_precip:.2f} inches." )
  print( f"Average precipitation: {avg_precip:.2f} inches." )
  print( "{} has the highest precipitation: {:.2f} inches.".format(*max_precip) )
  print( "{} has the lowest precipitation: {:.2f} inches.".format(*min_precip) )