# Unit 3 Project -  Storts, Chophy, Bascat

### *"I'm thinking of a five-letter word..."*

## Overview
Storts, Chophy, Bascat is a guessing game where a randomly selected word of a specific name is generated, and the user has a certain number of tries to guess the correct word. Similar to Wordle, the terminal will respond with gibberish words indicating the level of correctness.

This project utilizes program design, file input/output, and error checking to determine your understanding of creating complete programs.

---

## Key Requirements
By the end of this project, your program should allow for the following functionality:
- [ ] **Read in a file** containing english words. Using a predetermined value, store words of a certain length into a list.
- [ ] **Randomly select a word from the list** and use it to process input from the user.
- [ ] **Get a word input from the user**, and respond with the following:
	- The word *Storts* is printed if a specific letter in a word is correct, BUT in the wrong location.
	- The word *Chophy* is printed if a specific letter in a word is correct, AND in the right location.
	- The word *Bascat* is printed if no letters in the word meet either requirement.
	- Ensure the user can only guess words that are *the same length as the target word*
	- Extra Credit: Ensure the user can only guess valid english words. (Consider that we are utilizing a project file of english dictionary words) 
- [ ] **Process the output** correctly and efficiently
	- Clearly show to the user which letters are marked *Storts* and *Chophy*
	- Clearly show the user how many 'tries' they have left.
- [ ] **If the user has run out of attempts or correctly guesses the answer**, show them the 'end state' of the game ( Win or Loss ). 
	- Offer the user to play again, exit the game if they refuse.
- [ ] **Allow the user to change the difficulty**, this can be done one of two ways:
	- You can pre-set 'levels' by including different chances/word lengths as 'easy, medium, hard, etc.' and have your user select them.
	- You can have the user modify chances/word length directly, just ensure that each value is a valid option.
---
## Submission Guidelines
Please submit your file by pushing all changes to your assigned git repository. Your project submission should consist of **1** file:
1. lastname_scb.py - This project file should contain all of your code for the project. Be sure to include any additional assets you will need to actually run the game.
Additionally, include the following:
- **At least three** screenshots of terminal output done from your own testing. Include them in a folder labelled "Screenshots".
___
## Useful Links
- [Variables](https://www.w3schools.com/python/python_variables.asp) 
- [While Loops](https://www.w3schools.com/python/python_while_loops.asp#gsc.tab=0) 
- [For Loops](https://www.w3schools.com/python/python_for_loops.asp) 
- [Random](https://www.w3schools.com/python/module_random.asp)  
- [Functions](https://www.w3schools.com/python/python_functions.asp)
___
# Specification Grade Criteria

This project has a total of **30** points, **5** for each specification above. The chart below outlines what constitutes each point rating.

| Score | Problem Solving                                                                                                                                  |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| 5     | Response gives evidence of a complete understanding of the problem; is fully developed; is clearly communicated.                                 |
| 4     | Response gives the evidence of a clear understanding of the problem but contains minor errors or is not fully communicated.                      |
| 3     | Response gives evidence of a reasonable approach but indicates gaps in conceptual understanding. Explanations are incomplete, vague, or muddled. |
| 2     | Response gives some evidence of problem understanding but contains major programming or reasoning errors.                                        |
| 1     | No response or response is completely incorrect or irrelevant.                                                                                   |
