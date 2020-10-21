print("Title of program: MCQ revision program")
print()

counter = 0
score = 0
total_num_of_qn = 1


counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "What is the solvent in bubble tea?")
  print("   a) water")
  print("   b) tea")
  print("   c) tapioca pearls")
  print("   d) milk")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Correct, you at least have a brain!"
    tracker =1
    score +=1
  elif answer == "b":
    output = "Wrong. Tea is made with water and tea leaves."
    score -=1
  elif answer == "c":
    output = "Wrong. Pearls are the solute."
    score -=1
  elif answer == "d":
    output = "Wrong. Milk is made with water and milk powder."
    score -=1
  else:
    output = "Please choose a, b, c or d only."
  
  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
