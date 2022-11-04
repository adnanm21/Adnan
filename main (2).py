print("Hello, this is a quiz testing you on the capital cities of cetain countries!")
playing = input("Do you want to take the challenge?")
if playing != "yes":
  quit()
  
print("The challenge begins!") 

answer = input("What is the capital city of France? ")
if answer == "Paris":
  print("You are correct!")
else:
  print("You're incorrect, better luck next time!")

answer = input("What is the capital city of Barbados? ")
if answer == "Bridgetown":
  print("You are correct!")
else:
  print("You're incorrect, the answer is Bridgetown. Better luck next time!")

answer = input("What is the capital city of Canada? ")
if answer == "Ottawa":
  print("You are correct!")
else:
  print("You're incorrect, the answer is Ottawa. Better luck next time!")

answer = input("What is the capital city of Costa Rica? ")
if answer == "San Jose":
  print("You are correct!")
else:
  print("You're incorrect, the answer is San Jose. Better luck next time!")