print("This is the computer challenging you for a rock paper scissors game!")
playing = input("Do you accept this challenge?")
if playing != "yes":
  quit()
print("You've chosen to face the computers challenge!")  

answer = input("Please choose rock, paper or scissors.")
if answer == "rock":
  print("The computer is thinking...")
  print("You've suprisingly won!")
else:
  print("You're incorrect, better luck next time!")

answer = input("Please choose rock, paper or scissors.")
if answer == "Paper":
  print("The computer is deciding...")
  print("It was a tie!")
if answer == "rock":
  print("You've won, well done!")
else:
  print("You've lost, better luck next time!")

  answer = input("Please choose rock, paper or scissors.")
if answer == "Scissors":
  print("The computer is choosing...")
  print("You've lost, better luck next time.")
if answer == "rock":
  print("It's a tie!")
else:
  print("You've won! Well done!")


