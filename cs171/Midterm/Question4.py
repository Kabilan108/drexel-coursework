# CS 171 - Midterm Question 4 (12.9)
# Purpose: Function definition
# Author:  Tony Kabilan Okeke (tko35)
# Date:    02.07.2022

def determineBrightness(luminance):
    """
    This function characterizes the luminance values provided
    """

    if luminance < 10:
        out = "It's very dark!"
    elif luminance < 51:
        out = "It's a little dark"
    elif luminance < 200:
        out = "It's bright enough"
    elif luminance < 250:
        out = "It's getting brighter"
    else:
        out = "It's too bright!"

    return out