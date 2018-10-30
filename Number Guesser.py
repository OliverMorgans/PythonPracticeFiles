def guess_number():
  import random
  Answer = random.randint(0,11) 
  print "Guess what number I'm thinking of between 0 and 10!"
  Guess = input("Whats your guess? ")
  correct = False
  
  while not correct:
    Guess = input("Whats your guess? ")
    if Guess > 10:
      print "thats not in the range dummy"
    elif Guess < 0:
      print "thats not in the range dummy"
    elif Guess > Answer:
      print "guess lower dummy"
    elif Guess < Answer:
      print "guess higher dummy"
    elif Guess == Answer:
      print "Congratulations you did it you idiot"
      correct = True

guess_number()
