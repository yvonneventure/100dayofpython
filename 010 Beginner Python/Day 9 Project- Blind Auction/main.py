from replit import clear
#call clear() to clear the output in the console.
from art import logo
print(logo)
print("Welcome to the secret auction program.")
cont=True
auction={}
x=0
y=""
while cont==True:
  name=input("What is your name?:")
  bid=int(input("What is your bid?: $"))
  answer=input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if answer== "yes" :
    cont=True  
  elif answer=="no":
    cont=False
  clear()
  auction[name]=bid
  #print(auction)

for thing in auction:
  if x <=auction[thing]:
    x=auction[thing]
    y=thing
print(f"The winner is {y} with a bid of ${auction[y]}.")
  
