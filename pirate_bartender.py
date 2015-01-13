#  13 January 2015:  raw, starting point -- content notes from assignment

import random

# Sample random call
#beatles = ["John", "Paul", "George", "Ringo"]
## Print the name of a random Beatle
#print random.choice(beatles)

questions = {
  "strong": "Do ye like yer drinks strong, like the kraken?",
  "salty": "How about a salty tang, to remind ye of the briny deep?",
  "bitter": "Arrr ye a lubber what likes it bitter, as an old sea dog's harrrt?",
  "sour": "Maybe a bit of sour, like me captain in the morn?",
  "sweet": "Do ye take some sweetness with yer poison, me swabbie?",
  "fruity": "Arrr ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sour": ["chunk of grapefruit", "jigger of vinegar", "touch of lime juice"],
    "sweet": ["sugar cube", "spoonful of honey", "splash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

def style(questions):
  """Query user for flavor preferences"""
  prefs = {}
  for entry in questions:
    prefs[entry] = True if raw_input(questions[entry]+" ")[0].lower() == "y" else False
  return prefs

def mixer(prefs):
  """Build drink based upon user's flavor preferences"""
  # use random.choice to add ingredients to drink
  drink = []
  for choice in prefs:
    if prefs[choice] == True:
      drink.append(random.choice(ingredients[choice]))
  return drink

if __name__ == '__main__':
  print "Arrrrr!  Welcome to the Old Salt, matey!"
  print "Answer me questions and I'll bring ye a drink to quench yer thirst."
  print "If ye like the style, answer 'y' or 'yes' and it goes in yer drink."
  prefs = style(questions)
  drink = mixer(prefs)
  # Prepare drink
  for ing in drink[::1]:
    print ing # debug
  
  # Extra challenges
  #  Name the drinks
  #  Have another round
  
  # Extension exercises
  #  Multiple customers
  #  Stock control