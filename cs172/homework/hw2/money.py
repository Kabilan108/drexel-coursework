# File Name:   money.py
# Purpose:     Implements the Money class to represent a monetary value
# Author:      Tony Kabilan Okeke
# Date:        January 25, 2023


class Money:
    """
    Implementation of Money class

    Methods
    -------
    getDollars() -> int
        Return the number of dollars
    getCents() -> int
        Return the number of cents
    addDollars(value: int) -> None
        Add a given amount of dollars
    addCents(value: int) -> None
        Add a given amount of cents
    """

    def __init__(self, dollars: int=0, cents: int=0) -> None:
        """Constructor for Money Class"""

        self.__dollars = dollars
        self.__cents = cents

    def getDollars(self) -> int:
        """Return the number of dollars"""

        return self.__dollars

    def getCents(self) -> int:
        """Return the number of cents"""

        return self.__cents

    def addDollars(self, value: int) -> None:
        """Add a given amount of dollars"""

        self.__dollars += value
        return

    def addCents(self, value: int) -> None:
        """Add a given amount of cents"""

        cents = self.__cents + value
        self.__cents = cents % 100
        self.__dollars += cents // 100
        return

    def __add__(self, b):
        """Overload +"""

        cents = self.getCents() + b.getCents()
        dollars = self.getDollars() + b.getDollars() + cents // 100
        return Money(dollars, cents % 100)


    def __sub__(self, b):
        """Overload -"""

        cents = abs((self.getDollars()*100 + self.getCents()) - 
                    (b.getDollars()*100 + b.getCents()))
        return Money(cents // 100, cents % 100)

    def __mul__(self, multiplier: int):
        """Overload *"""

        cents = self.getCents() * multiplier
        dollars = self.getDollars() * multiplier + cents // 100
        return Money(dollars, cents % 100)

    def __str__(self):
        """Overload str"""

        return f"${self.getDollars()}.{self.getCents():02}" 

    def __eq__(self, b):
        """Overload =="""

        a = self.getDollars()*100 + self.getCents()
        b = b.getDollars()*100 + b.getCents()
        return a == b

    def __ne__(self, b):
        """Overload !="""

        a = self.getDollars()*100 + self.getCents()
        b = b.getDollars()*100 + b.getCents()
        return a != b

    def __lt__(self, b):
        """Overload <"""

        a = self.getDollars()*100 + self.getCents()
        b = b.getDollars()*100 + b.getCents()
        return a < b

    def __le__(self, b):
        """Overload <="""

        a = self.getDollars()*100 + self.getCents()
        b = b.getDollars()*100 + b.getCents()
        return a <= b

    def __gt__(self, b):
        """Overload >"""

        a = self.getDollars()*100 + self.getCents()
        b = b.getDollars()*100 + b.getCents()
        return a > b

    def __ge__(self, b):
        """Overload >="""

        a = self.getDollars()*100 + self.getCents()
        b = b.getDollars()*100 + b.getCents()
        return a >= b

    def __getitem__(self, key):
        """Overload []"""

        if key == 0:
            return self.getDollars()
        elif key == 1:
            return self.getCents()
        else:
            raise KeyError('Unassigned Key: Use 0 for dollars and 1 for cents.')

    def __repr__(self):
        return self.__str__()

