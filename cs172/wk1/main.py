#Program:     main.py
#Purpose:     Test the Coin class
#Author:      Adelaida Medlock
#Date:        March 28, 2022

# import the coin module so we can use the Coin class
import coin

# main routine
if __name__ == "__main__":
    
    # create an object from the Coin class
    myCoin = coin.Coin('Heads', 5)
    
    # display the Coin
    print(myCoin)
    print()
    
    # toss the Coin 5 times
    for i in range(1, 6) : 
        # toss the Coin
        print('I am tossing the coin...')
        myCoin.toss()
    
        # display the side of the coin that is facing up
        print('This side is up now:', myCoin.getSideup())
        print()

    # create a second Coin
    anotherCoin = coin.Coin('Tails', 25)
    
    # display the second coin
    print(anotherCoin)
