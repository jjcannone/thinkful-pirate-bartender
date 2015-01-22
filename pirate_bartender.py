#  13 January 2015:  now somewhat mature, no extras or extensions

import random

questions = {
  "strong": "Do ye like yer drinks strong, like the kraken?",
  "salty": "How about a salty tang, to remind ye o'the briny deep?",
  "bitter": "Arrr ye a lubber what likes it bitter, as an old sea dog's harrrt?",
  "sour": "Maybe a bit o'sour, like me captain in the morn?",
  "sweet": "Do ye take some sweetness with yer poison, me swabbie?",
  "fruity": "Arrr ye one fer a fruity finish?"
}

ingredients = {
    "strong": ["glug o'rum", "slug o'whisky", "splash o'gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher o'bacon"],
    "bitter": ["shake o'bitters", "splash o'tonic", "twist o'lemon peel"],
    "sour": ["chunk o'grapefruit", "jigger o'vinegar", "touch o'lime juice"],
    "sweet": ["sugar cube", "spoonful o'honey", "splash o'cola"],
    "fruity": ["slice o'orange", "dash o'cassis", "cherry on top"]
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
  if len(drink) > 0:
    ings = drink[0] 
    for ing in drink[1:-1]:
      print ing # debug
      ings += ", " + ing
    if len(drink) > 1:
      ings += ", and " + drink[len(drink) -1]
    print "Here's yer drink -- a pleasant mix o'{}".format(ings)
  else:
    print "Ye didna order anything?  Arrr ye scared of Old Pete?"
  
  # Extra challenges
  #  Name the drinks
  #  Have another round
  
  # Extension exercises
  #  Multiple customers
  #  Stock control