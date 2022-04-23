#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level=input("Choose a difficulty. Type 'easy' or 'hard': ")
if level=='hard':
  attempt=5 
elif level=='easy':
  attempt=10

cont=True
while cont==True:
  print(f"You have {attempt} attempts remaining to guess.")
  guess=int(input("Make a guess: "))
  
  n1=random.randint(1,100)
  #print(n1)
  if guess>n1:
    print("Too high.")
    
    attempt-=1
    if attempt==0:
      cont=False
      print(f"You lose, the number is {n1}, you went out of chances.")  
    print("Guess again.")
  elif guess<n1:
    print("Too low.")
    
    attempt-=1
    if attempt==0:
      cont=False
      print(f"You lose, the number is {n1}, you went out of chances.") 
    print("Guess again.")
  else:
    print(f"You got it. The answer is {n1}.")
    cont=False

