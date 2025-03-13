import random

#first loop
while True:
  
  #bbg is what you input 

  bbg = input('guessr ').lower 
  #.lower thakle if someone writes in caps tahole itll make it small letter
  # were working with small letters

  # now computer makes a choice from a list of words
  bbg2 = random.choice(['rock','paper','scissors'])

  #this line shows what the computer chose
  print("i chose",bbg2)

  #ekhane compare kore what happens
  # bbg comes before bbg2 
  # btw bbg stands for babygirl and not python technical term
  # so as bbg (your input) is rock and bbg2 (computer inout) is scissors you win
  # erokom combination kore 
  # if these combinations arent tgere suppose duijon e same tahole tie
  # ar since matro 3 ta outcome we can just say else (aro kichu hole) you lose

  
  print("you winn lessgoo" 
        if (bbg,bbg2) in [('rock','scissors'),('paper','rock'),('scissors','paper')] 
        else "its a tie" if bbg == bbg2 
        else "you lose noibie boobie")
                        
                        
