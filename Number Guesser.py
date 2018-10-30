def guess_number():
  import random
  Answer = random.randint(0,11) 
  print ("Guess what number I'm thinking of between 0 and 10!")
  correct = False
  
  while not correct:
    Guess = int(input("Whats your guess? "))
    if Guess > 10:
      print ("thats not in the range")
    elif Guess < 0:
      print ("thats not in the range")
    elif Guess > Answer:
      print ("guess lower")
    elif Guess < Answer:
      print ("guess higher")
    elif Guess == Answer:
      print ("Congratulations you did it")
      correct = True

guess_number()
