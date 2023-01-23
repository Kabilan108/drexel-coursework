"""
Monty Hall Simulation
"""

# Imports


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

    """
    Pseudocode:

    foreach iteration
        - randomly determine which door has the car.
        - player picks a door randomly.
        - among the two doors the player did not pick, randomly discard the one
          that doesn't have the car.
        - apply the strategy
        - if the player wins, count it as a win.
    calculate the winning ratio.
    """


    # YOUR CODE HERE
    raise NotImplementedError()