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

<div style="background-color:#cb3c39">
Redefine alignment of two sequences so we can use the best alignment of shorter sequences and build our way up to the larger problem.
</div>
Let’s consider the game described below,
<div style="background-color:#f1f1ef">
Consider a boardgame with a certain amount of money in each square. You are asked to start from the top left corner, and move your way down to the bottom right corner.
→ From each square, you can make one of three moves, go down, right, or diagonally to the right.
→ When you make a diagonal move, you collect the money on the square.
→ When you make a down or right move, you do not collect the money, and you receive a $1 penalty.
→ You always keep the money in the top left corner.
→ The game ends when you reach the bottom right corner.
</div>