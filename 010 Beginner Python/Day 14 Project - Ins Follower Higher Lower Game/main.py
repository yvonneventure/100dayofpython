from game_data import data
import random
#print(len(data))

#random get item from list, form the info in dictionary to string, then print
def get():
  item1=random.choice(data)
  name=item1["name"]
  desc=item1["description"]
  count=int(item1["follower_count"])
  country=item1["country"]
  return count, f"{name}, {desc}, from {country}"



#print(f"{count1},{string1},{count2},{string2}")
#get A
score=0
game=True
count,string=get()
list=[]
lista=[count,string]
list.append(lista)
#print(list)

#get B
while game==True:
  if score!=0: 
    
    print(f"You win, your current score is {score} ")
  print(f"Compare A : {list[0][1]}")
  print("vs.")
  count,string=get()
  lista=[count,string]
  list.append(lista)
  #print(list)

  # list.append(count)
  # list.append(string)
  print(f"Against B: {list[1][1]}")
  #compare A and B
  guess=input("Who has more followers? Type 'A' or 'B'. ")
  
  
  if list[0][0]>=list[1][0] and guess=="A":
    score+=1
    # print(f"You win, your current score is {score} ")
    del list[0]
    #print(list)
  elif list[0][0]<=list[1][0] and guess=="B":
    score+=1
    # print(f"You win, your current score is {score} ")
    del list[1]
    
    #print(list) 
  else:
    game=False
    print(f"You lose, your final score is {score} ")

#if (count1>=count2 and guess=="A") or (count2>=count1 and guess=="B"):
#   score+=1
#   print(f"You win, your current score is {score} ")
 #B should be A, and then random another B

  
  
  
# print(f"Compare A: {name}, {desc}, from {country}")
# print("vs.")




#let player make a guess, check if right, score+1, wrong end the game, otherwise loop