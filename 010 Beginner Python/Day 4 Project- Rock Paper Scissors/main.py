rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
you=input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n")
you=int(you)
import random
computer=random.randint(0,2)
list=[rock,paper,scissors]
print(list[you])
print(f"Computer chose: \n{list[computer]}\n")
if (you==0 and computer==2) or (you==1 and computer==0) or (you==2 and computer==1):
  print("You win")
elif you==computer:
  print("You draw")
else:
  print("You lose")
  
