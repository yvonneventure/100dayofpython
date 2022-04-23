
#calculator

#add, substract, multiply, divide
def add(n1,n2):
  """Docstrings -- where you input description of your function to show up if typing
  this is mutiline, but has to be the 1st line in function"""
  return n1+n2
def substract(n1,n2):
  return n1-n2
def multiply(n1,n2):
  return n1*n2
def divide(n1,n2):
  return n1/n2
#create a operation dictionary, with key are the signs, and values are the function name
operations={
  "+":add,
  "-":substract,
  "*":multiply,
  "/":divide,
}


def calculator():
  new=True
  num1=int(input("what's the 1st number?"))

  #loop start
  while new:
    
    num2=int(input("what's next number?"))
    for operator in operations:
      print(operator)
    operation=input("pick a operation: ")
  #call the function from dictionary
  #answer=operations[operation](num1,num2)
    calculation=operations[operation]
    answer=int(calculation(num1,num2))
    print(f"{num1} {operation} {num2} = {answer}")
  
    go=input("type 'y' to continue, or 'n' to start a new calculation.\n")
    
    if go=="n":
      new=False
      calculator() 
      #call itself, needs a condition, otherwise will be infinite loop
      #called recursion, this kind of function cannot have input and output
    elif go=="y":
      num1=answer
      

calculator() 
