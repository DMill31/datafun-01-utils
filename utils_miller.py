"""
Module: utils_miller

Purpose: Reusable Module for My Analytics Projects

Description: This module provides a byline for my first analytics project. 
When we work hard to write useful code, we want it to be reusable.
A good byline could be used in every Python analytics project we do.

Author: Daniel Miller
Original Author: Denise Case

"""

#####################################
# Import Modules
#####################################

# Import helpful modules from the Python Standard library
# See more at: https://docs.python.org/3/library/

import statistics  # provides mean(), stdev() and more....

#####################################
# Declare Global Variables
#####################################

# declare a boolean variable (has a value True or False)
is_in_wisconsin: bool = True

# declare an integer variable 
years_in_wisconsin: int = 16

# declare a floating point variable
average_wind_speed_mph: float = 10.6


# declare a list of strings
wisconsin_cities: list = ["Madison", "Milwaukee", "Green Bay"]

# declare a list of numbers so we can illustrate statistics skills 
daily_max_temp_fahrenheit: list = [21, 34, 40, 32, 8]

# Calculate basic statistics using built-in Python functions and the statistics module
# TODO: Replace these variable names with the variable name of your own numeric list
min_score: float = min(client_satisfaction_scores)  
max_score: float = max(client_satisfaction_scores)  
mean_score: float = statistics.mean(client_satisfaction_scores)  
stdev_score: float = statistics.stdev(client_satisfaction_scores)

# Use a Python formatted string (f-string) to show information
# TODO: Modify the variables in the byline to use your variable names
byline: str = f"""
---------------------------------------------------------
Wisconsin: Some Fun Personal Data
---------------------------------------------------------
Is in Wisconsin:                          {is_in_wisconsin}
Years in Wisconsin:                       {years_in_wisconsin}
Wisconsin Cities:                         {wisconsin_cities}
Daily Maximum Temperature in Fahrenheit:  {daily_max_temp_fahrenheit}
Minimum Daily Maximum Temperature:        {min_score}
Maximum Daily Maximum Temperature:        {max_score}
Mean Daily Maximum Temperature:           {mean_score:.2f}
Standard Deviation of Temperatures:       {stdev_score:.2f}
"""

#####################################
# Define global functions (resuable instructions)
#####################################

def get_byline() -> str:
    '''
    Get a byline for my analytics projects.
       
    Returns a string byline that illustrates my specific skills.

    A function is a block of code that performs a task.
    This function just returns our byline.
    We can call this (or other functions) in later modules 
    so we can write it once and reuse it. 
    We use a type hint to indicate this function returns a string
    (that is, it has a Python type of str).
    It doesn't need any additional information passed in, 
    so there's nothing needed inside the parentheses.
    Everything afer the colon must be indented consistently (usually 4 spaces)
    '''
    return byline

#####################################
# Define main function for this module.
#####################################

def main() -> None:
    '''
    Print results of get_byline() when main() is called.

    This function just prints the byline to the console when we run this as a script.
    The type hint indicates this function doesn't return anything when called 
    (that is, it has a Python type of None).
    It doesn't need any additional information passed in, 
    so there's nothing inside the parentheses.
    Everything afer the colon must be indented consistently (usually 4 spaces)
    '''

    print("Starting........")
    print(get_byline())
    print("Complete.......")

#####################################
# Conditional Execution
#####################################

# If we are running this file as a script then call main()
# and verify our code works as expected.

if __name__ == '__main__':
    main()

#TODO: Run this as a script and verify all code works as intended.
