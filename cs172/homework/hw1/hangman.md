Hangman
In this assignment we will write a version of the Hangman game using Python.

In our version of the game the user will play against the computer. Here is the set of modified rules to play against the computer:

The computer will choose a secret random word from a list of words stored in a data file.

The player will try to guess the secret word by entering one letter in each turn.

The computer will give feedback to the player by indicating whether:

The letter entered by the player does not exist in the secret word, or
The letter entered by the player exists in the secret word. In this case the program will show the user the position of the letter within the word.
The player has unlimited number of turns until they have guessed the word. At that point program tell the user how many turns it took to guess the secret word.

Here are a few examples of the feedback the program will give to the player:

Example #1

Computer’s secret word: python

Player’s letter: a

Computer’s response:

a is not in my secret word. 
Guess another letter.
Example #2

Computer’s secret word: python

Player’s letter: n

Computer’s response:

n is part of my secret word.
-----n
The response -----n shows that the letter n is part of the secret word, as well as its position within the secret word.

Example#3

Computer’s secret word: tooth

Player’s letter: o

Computer’s response:

o is part of my secret word.
-oo--
The response -oo-- shows that the letter o is part of the secret word, as well as all its locations within the secret word. Since the letter o appears twice in the secret word tooth the the letter o is shown twice in feedback provided by the computer.

Example #4 In this example we are assuming the player has already guess some letters correctly.

Computer’s secret word: chocolate

Player’s letter: c

Computer’s response:

c is part of my secret word.
c-oco---e
The response c-oco---e shows that the letter c is part of the secret word, as well as all its locations within the secret word. The user had already guessed correctly that the letters o and e are part of the secret word (in previous turns), so the feedback includes those letters in their proper locations.

Besides the rules, here are some additional specifications:

Your program must ask the user to enter the name of data file and validate that the file exists and that it can be open. The file contains words, one word per line.

Your program must open the file for reading and randomly choose a secret word from the words found in the file. The secret word should be randomly chosen for each new game. You should import the module random. You will be using the following functions:

random.seed(seed_value) seeds the random number generator using the given seed_value. For testing purposes, use the seed value 15, which will cause the computer to choose the same random value every time the program runs.
random.randint(a, b) returns a random number between a and b (inclusive). You could use this function to generate a random index value use that index to obtain the secret word.
Alternatively, you could use random.choice(list). This function returns a random item from a list. You could use this function (instead of randint) to obtain the secret word.
The program then should ask the player to enter a letter and provide the corresponding feedback (as shown in the examples above)

Your program must include a loop so that the player can repeatedly enter guesses and received feedback from the program. When the player has guessed all the letters in the secret word the program prints out a congratulation and tells the user how many guesses were required.

Your solution must include at the very least the following functions:

findMatches(word, letter): This function receives a string that contains the secret word, and a string that contains a letter that exists in the word. The purpose of this function is to find where letter appears in word. This function returns a string made of the - character marking the positions where letter does not appear, and letter in positions where letter is found in the word. For example findMatches('tooth', 'o') would return the string: '-oo--'. Here is another example: findMatches('candy', 'a') would return the string: '-a---'.

merge(word1, word2): This function receives two string's. The purpose of this function is to parse both strings received as parameters and produce a resulting string that combines the letters and '-' from both strings, in the corresponding positions. For example, merge('p----n', 'p-th--') would return the string 'p-th-n'. Here is another example: merge('--o-o---e', 'c--c-----') would return the string 'c-oco---e'.

Please make sure you include a header comment at the top of your file, as well as comments before each function.

Below there’s a sample run:

Enter name of the data file: data.txt
Error: that file does not exist. Try again.
Enter name of the data file: words1.txt
I have a 8 letter word, try to guess it.
You will enter one letter at the time.
Enter a letter to see if it's in the word: a
a is not in my secret word.
Guess another letter.
Enter a letter to see if it's in the word: e
e is part of my secret word.
------e-
Enter a letter to see if it's in the word: i
i is not in my secret word.
Guess another letter.
Enter a letter to see if it's in the word: o
o is part of my secret word.
-o----e-
Enter a letter to see if it's in the word: u
u is part of my secret word.
-o--u-e-
Enter a letter to see if it's in the word: t
t is part of my secret word.
-o--ute-
Enter a letter to see if it's in the word: r
r is part of my secret word.
-o--uter
Enter a letter to see if it's in the word: c
c is part of my secret word.
co--uter
Enter a letter to see if it's in the word: m
m is part of my secret word.
com-uter
Enter a letter to see if it's in the word: p
p is part of my secret word.
computer
Congratulations, you guessed my secret word!
It took you 10 turns to guess my secret word.
Notes:

You may find the following site useful to compare your output against the expected program output: Diffchecker
The purpose of this problem is to practice writing functions, reading data from files, and using modules.
Please make sure to submit a well-written program. Good identifier names, useful comments, and spacing will be some of the criteria that will be used when grading this assignment.
This assignment can be and must be solved using only the materials that have been discussed in class. Do not look for alternative methods that have not been covered as part of this course.
How your program will be graded:

correctness: the program works and performs all tasks correctly: 60% (autograded by Zybooks)
complies with requirements (it properly implements required functions, input validation, loops/conditionals, random module ): 25% (TAs)
code style: good variable names, comments, proper indentation and spacing: 15% (TAs)
