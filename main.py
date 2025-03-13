import random
while True:
  bbg = input('guessr ').lower
  bbg2 = random.choice(['rock','paper','scissors'])
  print("i chose",bbg2)
  print("you winn lessgoo" if (bbg,bbg2) in [('rock','scissors'),('paper','rock'),('scissors','paper')] else "its a tie" if bbg == bbg2 else "you lose noibie boobie")
                        
                        
