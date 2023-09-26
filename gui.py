from asyncio import _enter_task
from ctypes import alignment
from tkinter import *
from wordle import *

class Gui:
  def __init__(self, wordle):
    self.w = wordle
    self.guessesLeft = 5
    self.window = Tk()
    self.window.geometry("600x700")
    self.window.title("Wordle")
    self.window.config(background = "black")
    self.text = Text(self.window, 
                    font = ("Helvetica Neue", 50),
                    height = 1,
                    width = 9)
    self.text.pack()
    self.button = Button(self.window, command = self.submit, text="submit")
    self.button.pack()
    self.window.mainloop()
  
  # called when the submit button is hit
  # calls checkGuess to see if the guess is valid. 
  def submit(self):
    guess = self.text.get("1.0", END)
    guess = guess[0:len(guess)-1]
    print ("Guess is " + guess) # len(guess)-1 gets rid of the '\n' at the end
    print ("checkGuess() called")
    self.checkGuess(guess)
    

  def checkGuess(self, guess):
    if (self.w.validGuess(guess)): 
      print("Valid Guess, submitGuess() called")
      self.submitGuess(guess)
    else:
      print("Invalid Guess, awaiting valid guess")

  # decrements guessesLeft
  # gets the colors of the users guess
  # checks if the user is a winner or not
  # if not, displays colors
  def submitGuess(self, guess):
    self.guessesLeft -= 1
    colors = self.w.getColors(guess)
    print("calling displayColors()")
    self.displayColors(guess, colors)
    if (self.w.winner(colors)):
      print("You are a winner. winner() called")
      self.winner()
    else:
      print("Guess was not correct")
      if (self.guessesLeft == 0):
        print("You are out of guesses. Game over")
        quit()
    
  # shows the user the results of their guess
  def displayColors(self, guess, colors):
    output = self.w.getResults(guess, colors)
    print(output)
  
    
  # eventually will display some sort of graphic for a win
  def winner(self):
    quit()

# Create instance of wordle
w = Wordle()

# print the answer to the console
print (w.getAnswer()) 

# run the program
g = Gui(w)
