
# Imports
import random


def hwbayes_montyhall(strategy: int, trials: int) -> float:
    """
    Monty Hall Simulation

    In this function, you need to simulate the game for `trials` many times
    and return the ratio of the times the player wins under the given strategy.

    Parameters
    ----------
    strategy : int
        One of 0, 1, 2, with the following meanings:
        0: never switch door
        1: always switch door
        2: switch door at random (switch or stay with equal probability)
    trials : int
        Number of times you execute the game.

    Returns
    -------
    float
       Winning ratio of the player under the given strategy.
    """

    if strategy not in [0, 1, 2]:
        raise ValueError("Invalid strategy.")
    if trials < 1:
        raise ValueError("Invalid trials.")

    wins = 0  # Win counter

    for _ in range(trials):
        doors = [1, 2, 3]

        # Randomly place a car behind one of the doors
        car = random.choice(doors)

        # Randomly pick a door by the player
        chosen = random.choice(doors)

        # Doors not picked by the player
        other_doors = [d for d in doors if d not in [car, chosen]]

        # Discard one of the other doors that does not have the car
        discard = random.choice(other_doors)
        doors.remove(discard)

        # Implement strategies
        if strategy == 0:  # never switch door
            final = chosen
        elif strategy == 1:  # always switch door
            final = [d for d in doors if d != chosen][0]
        elif strategy == 2:  # switch door at random
            final = random.choice(doors)
        else:
            raise ValueError("Invalid strategy.")

        # Check if the player wins
        wins += int(final == car)

    return wins / trials * 100
