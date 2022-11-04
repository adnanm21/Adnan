print("Hello! This is a number guessing game!")
print("I will ask you to guess between a range of numbers and if you're correct, you win!!!")
playing = input("Do you want to play?")
if playing !="yes":
  quit()

print("You've accepted the challenge!")
answer = input("Guess a random number between the number 4-18.")
if answer == "10":
  print("Surpisingly you are correct!")
else:
  print("You're incorrect, the answer is 10.")
answer = input("Guess a random number between the number 9-23.")
if answer == "14":
  print("You actually got it correct!")
else:
  print("You're incorrect, the answer is 14.")
answer = input("Guess a random number between the number 19-21.")
if answer == "20":
  print("Shockingly you are correct!")
else:
  print("You're incorrect, the answer is 70.")
answer = input("Guess a random number between the number 50-100.")
if answer == "70":
  print("You are correct!")
else:
  print("You're incorrect, the answer is 70.")
  
  
