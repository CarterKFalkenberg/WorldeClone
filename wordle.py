from random import randint
from termcolor import colored

class Wordle:
  def __init__(self):
    # create list of possible answers and guesses 
    answers_file = open("answers.txt")
    guesses_file = open("guesses.txt")
    self.answers = answers_file.read().split('\n')
    self.guesses = guesses_file.read().split('\n')
    answers_file.close()
    guesses_file.close()
    
    # pick a random word for the answer
    self.answer = self.answers[randint(0, len(self.answers)-1)]


  # returns an array of the colors based on a guess and the answer
  def getColors(self, guess):
    # track colors and which letters are accoutned for
    colors = ["red", "red", "red", "red", "red"]
    usedAnsChars = [False, False, False, False, False] 
    # start with green
    for char in range(5):
      if guess[char] == self.answer[char]:
        colors[char] = "green"
        usedAnsChars[char] = True
    # then yellow
    for guessChar in range(5):
      if colors[guessChar] == "green":
        continue
      for answerChar in range(5):
        # ignore answer characters that we already accounted for
        if usedAnsChars[answerChar]:
          continue
        # check if yellow
        if (guess[guessChar] == self.answer[answerChar]):
          colors[guessChar] = "yellow"
          usedAnsChars[answerChar] = True
    return colors
  
  # returns true if the guess is valid, false otherwise
  def validGuess(self, guess):
    return guess in self.guesses or guess in self.answers

  # returns an array len 2. The first element is a boolean, the second a string
  # takes an array of colors and the guess
  # returns true as first element if they are all green
  # returns a string with each letter as the colors they should be
  def getResults(self, guess, colors):
    results = ""
    for i in range(5):
      results += colored(guess[i], colors[i])
    return results + "\n"

  def winner(self, colors):
    for i in colors:
      if i != "green":
        return False
    return True
      

  def getAnswer(self):
    return self.answer