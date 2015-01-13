#  13 January 2015:  raw, starting point -- content notes from assignment

import random

# Sample random call
#beatles = ["John", "Paul", "George", "Ringo"]
## Print the name of a random Beatle
#print random.choice(beatles)

# Thinkful Default Questions
questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}


def style():
  # iterate over questions
  # build dictionary of responses
  # accept "y" or "yes" as True; otherwise, False
  # return new dict (prefs)
  # hint: use raw_input() to help
  prefs = {}
  return prefs

def mixer(prefs):
  # use random.choice to add ingredients to drink
  drink = []
  return drink


if __name__ == '__main__':
  # Call two functions (style and ingredients) in order
  prefs = style()
  # Prepare drink
  
  # Extra challenges
  #  Name the drinks
  #  Have another round
  
  # Extension exercises
  #  Multiple customers
  #  Stock control