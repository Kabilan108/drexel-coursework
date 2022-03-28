# CS 171 - Final Question 3 (20.3)
# Purpose: Write a recursive function tha returns True only when a string
#          contains upper case letters only between the start and stop indexes
# Author:  Tony Kabilan Okeke (tko35)
# Date:    03.15.2022

def all_capital(string, start, stop):
    # Base case: empty string
    if start > stop:
        return True

    #? Are we allowed to use the isupper() method?
    #return string[start].isupper() and all_capital(string, start+1, stop)
    return 'A' <= string[start] <= 'Z' and all_capital(string, start+1, stop)


if __name__ == "__main__":
    string = "AAAbbbAcfGGGAA"
    print("all_capital (string, 6, 4) ->", all_capital(string, 6, 4) )  
    print("all_capital (string, 0, 2) ->", all_capital(string, 0, 2) )  
    print("all_capital (string, 6, 6) ->", all_capital(string, 6, 6) )  
    print("all_capital (string, 9, 13 ->", all_capital(string, 9, 13))  
    print("all_capital (string, 1, 7) ->", all_capital(string, 1, 7) )  
    print("all_capital (string, 0, 13 ->", all_capital(string, 0, 13))  
    print("all_capital (string, 2, 3) ->", all_capital(string, 2, 3) )  