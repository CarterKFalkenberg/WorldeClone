from wordle import *
from gui import *

# create an instance of wordle and the Gui
w = Wordle()
print(w.getAnswer()) # for testing purposes
g = Gui()

# start the game
result = ""
for i in range(1, 7):
  # get guess from user, make sure it is valid
  guess = g.getAnswer()
  while not w.validGuess(guess):
    # quick exit command for testing purposes
    if (guess == "exit"):
      quit()
    guess = g.getAnswer()
    print (f"guess is {guess}")
  # show user the colors / show user how good their guess was
  colors = w.getColors(guess)
  results = w.getResults(guess, colors) # array of [winner boolean, output string]
  winner = w.winner(colors)
  output = results[1]
  print(output)
  if (winner):
    if i == 1:
      print ("Wow... You solved it in 1 guess!")
    elif i < 6:
      print ("Congrats. You solved it in %d guesses" %i)
    else:
      print ("Whew... You barely got it! That took 6 guesses")
    break
  if (not winner):
   print ("Nice try, the answer was " + w.getAnswer())
