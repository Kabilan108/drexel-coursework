# Sequence Alignment

This is the problem of taking two DNA or Protein sequences and matching them up character by character with the goal of matching identical or similar characters together.

- Gaps are introduced when a character doesn’t have a good match in the other sequence.
- The quality of alignments are determined using an alignment score - usually additive.
    - Based on some criteria, e.g. Matches = +1, Mis-match = -1, Gap = -1.
    - There are different ways of defining the alignment score.
    - The goal of sequence alignment is to find a pairing that gives the maximum alignment score.
    - Need Efficient way to identify pairing with maximum score, without performing an exhaustive search - this would be exponentially harder with longer sequences.
        - **Dynamic Programming** - the most commonly used algorithm for sequence alignment.

## Dynamic Programming

Algorithm based on reusing solutions to smaller problems - it is an optimization over plain recursion.

>Redefine alignment of two sequences so we can use the best alignment of shorter sequences and build our way up to the larger problem.

Let’s consider the game described below,
>Consider a boardgame with a certain amount of money in each square. You are asked to start from the top left corner, and move your way down to the bottom right corner.  
- From each square, you can make one of three moves, go down, right, or diagonally to the right.  
- When you make a diagonal move, you collect the money on the square.
- When you make a down or right move, you do not collect the money, and you receive a $1 penalty.
- You always keep the money in the top left corner.
- The game ends when you reach the bottom right corner.

The goal of the game is to find the path which yields the most money. For smaller boards like the one below, this is easy.

|   |    |   |
|---|----|---|
| 5 | 2  | 5 |
| 6 | 3  | 4 |
| 3 | 12 | 2 |

For a larger board, the task becomes much more challenging because the number of possible paths increases exponentially.

|||||||||||
|----|---|----|---|----|----|---|---|----|----|
| 3  | 7 | 8  | 8 | 7  | 6  | 8 | 5 | 2  | 10 |
| 5  | 3 | 7  | 4 | 2  | 7  | 3 | 9 | 10 | 3  |
| 6  | 7 | 1  | 8 | 8  | 6  | 2 | 9 | 7  | 2  |
| 5  | 7 | 7  | 5 | 3  | 5  | 7 | 3 | 5  | 2  |
| 9  | 1 | 4  | 1 | 10 | 7  | 5 | 7 | 7  | 1  |
| 6  | 3 | 10 | 2 | 3  | 7  | 5 | 6 | 6  | 5  |
| 10 | 3 | 1  | 8 | 8  | 7  | 7 | 6 | 7  | 5  |
| 7  | 7 | 5  | 5 | 2  | 7  | 8 | 9 | 6  | 4  |
| 10 | 9 | 5  | 2 | 3  | 10 | 4 | 3 | 8  | 5  |
| 3  | 4 | 5  | 4 | 1  | 3  | 7 | 4 | 6  | 7  |

We need to find an approach that will reliably identify the best path in a reasonable amount of time.
We will use dynamic programming to derive our solution - this will allow us to determine the solution to the larger board based on solutions to smaller ones.

>**Solution Path**
> - Iterate through 2 matrices, storing ideal scores in both cases
> - store ideal moves 
> - back track through DP table to determine ideal score
> - Max alignment score is in bottom right corner

For python, each function must be in its own `.py` file
Do not put all python functions in one module.
Alternatively, define all functions in `Jupyter` notebook
Use `%reload` magic to reload modules