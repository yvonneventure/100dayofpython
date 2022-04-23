# Beginner Level Python Notes - Day 1 to Day 14


### Day 1 - Print, String Manipulation, Input, Variable

 1.1 `print( )` function, double quotes vs. single quotes
```python
print(“hello world!”)✅
print(‘hello world!’)✅
print("print('hello world’)”)✅
print(‘print("hello world”)’)✅
print(“print("hello world")”)❌
print(‘print('hello world')’)❌
```

 1.2 String manipulation
* `\n`for new line
```python
  print(“hello world\nhellonworld”)
  ```
* `+` for concat strings
```python
  print("hello"+"world")
 ```

 1.3 `input()` to show a prompt and ask input from user

 1.4 `#` for comment in python

 1.5 variable naming rules:

* use underscore`_` in variable name

* can use number at the end of the variable name

* cannot use function name as  your variable name



### Day 2 - Data Types, Number Operations

1. Data Types
  * `str` for string
    * like "Hello" has positions, and position always start at 0
    * position use a `[ ]` to specify has to be used within quotes
    * `+` in strings are concat, `+` in numbers are calculation
    
  * `int` for integer
    * numbers without decimal place, either negative or positive
    * underscore `_`used as thousand separator like 1,000,000
  
  * `float` for numbers with decimal place
  
  * `boolean` for Boolean `True` and `False`
    * `True` and `False` has to have first letter capitalized
    * Don't need quotes around it

2. Data Type Checking and Type Conversion

* Type Checking use `type()` function

* Type conversion
  * `str()` convert to string
  * `int()` convert to integer
  * `float()` convert to float number


3.Math Operations: `+`, `-`, `*`, `/`, and `x ** y` for x to the power y calculation

 - Division `/` always return a float data type
 
 - `%` called modula, will give you the reminder of the division : eg. `7 % 3 = 1`

 - Order of execution priority : PEMDAS
   - 1. Paranthesis `()`
   - 2. Exponents `**`
   - 3. Multiplication or Division `*` or `/`
   - 4. Addition or Submstraction `+` `-`
  > Same order will process from left to right
 
 - Shorthand for number manipulation
   - instead of use `a=a+2` we can use `a+=2`
   - same for `*=` `-=` `\=`

4. f-string
  - f-string allows you to not change data type and output like normal string
  - usually used with variable, and variable use `{}`
  - `print(f”My score is {score}")`

5. Number Manipulation
```python
print(int(8/3))  # chop off what's after decimal
print(round(8/3), 2)  # round to 2 decimal places
print(8//3)   # round down, works like floor function
{:0.2f} .format(9/2)  # if like 9/2=4.5, there's no way to round to 2 decimal place, then use this to format numbers

```

### Day 3 - Control Flow, Logic Operator

1. Conditional statement if/else

- comparison operator
 - `=` is assign what's on the right to the left
 - `==` is check equality of what on the right with what’s on the right
 - `!=` is not equal to 
  > - the condition statement should return a `True` or `False`, this will give you a hint whether the condition statement is correct
  > - indentation is important in `if/else` statement, it marks what code block will be executed, and you will get an indentation error if you you are doing it wrong

![flow chart 1](image.jpg)


```python

if age == 12:
     do this
else:
    do this 

```

2. Nested if statement (mulitple layers of condition has to be met)

![flow chart 2](image.jpg)

```python

 if height>120:
     if age>18:
        print("ticket is $12")
     else:
        print("ticket is $7")
   else:
      print("you cannot ride") 

```


3. `elif` statement  (choice or multiple options at the same level/layer)

![flow chart 3](image.jpg)

```python
 if height>120:
     if age>18:
        print("ticket is $12")
     elif age>12 and age<18:
          print("ticket is $7")
     else:
        print("ticket is $5")
   else:
      print("you cannot ride")

```

4. multiple if statement (no matter what the previous condition; order of execution)


![flow chart 4](image.jpg)

```python
  # indentation is very important, will change the order of execution
  if height>120:
     if age>18:
        print("ticket is $12")
     elif age>12 and age<18:
          print("ticket is $7")
      else:
        print("ticket is $5")
  #below if is after the execution of the above if and as a seperate condition (not relate to age)      
      if want ticket:
        print("ticket+$3")
     #whether you buy or not buy ticket, you will need to print out line 14 so here don't need to put else, pay attention to the indentation
    print("your total ticket would be xx")
   else:
      print("you cannot ride")
```



5. logic operator `and`, `or`, `not`

```python

if age == 12 and height<180 :
     do this
else:
    do this 

```



### Day 4 - Randomisation, Python List


1.  Creat randomness using Randome Module

```python
import random
print(random.randint(1,10))     #return a random number between 1 and 10 - [1,10]
print(random.random())         #can only return a random float between [0,1) -not include 1
print(random.random()*5)      # now give the ability to return a float [0,5)
```

2. Create Module and use it 
```python
import yvonne                        #module yvonne created by myself, with one variable in it yvonne="smile"
print(yvonne.yvonne)                   #  print(ModuleName.VarName)
```


3. [List - Data Structure](https://docs.python.org/3/tutorial/datastructures.html)

```python
#list - data structure
fruit=["apple","pear","banana","cherry"]     # way to create a list use []
print(fruit)
veggies = []                        # way to create an empty list
fruit=["apple",1,"banana","cherry"]            # list can have different data types
print(fruit)                                             #print the entire list
print(fruit[0])                                         # position start at 0
print(fruit[-1])                  # the last one in the list, index/position can be negative
fruit[1]="pear"                 # offset : change the value at position 1 to a new value
print(fruit)
fruit.append("c")             #append one value to the list
print(fruit)
fruit.extend(["a","b"])      # append a list to the existing list
print(fruit)
len(fruit)                      # return how many items in the list

random.choice(fruit)    # will pick randomly from the list
```


4. Nested List

- items has an order in the list, called index, will be used to call them out, so the order is very important

```python
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]       # a nested list that has two lists
print(dirty_dozen[0]) 
print(dirty_dozen[1]) 
# first bracket [1] get the list of position 1, which is vegetable list
print(dirty_dozen[1][2]) # the index 2 of the index 1 list => the 3rd item in the 2nd list, which is tomatos

```



### Day 5 - For Loops


1. For loops in a list

```python
fruits=["apple","pear","orange"]
#"fruit" here is not defined before, but for loops defined it automatically
for fruit in fruits :
  print(fruit)
#indentation is very important in for loops
print(fruit)
```

2. For Loops with `range()`

```python
#for loops with range( ),range is getting number [1,5) include 1 but not include 5;
#to include 5, should use range(1,6), default step is 1
#range(1,5,2) meaning numbers between 1 and 4,each add 2 ==>result is 1,3
for i in range(1,5):
 print(i)
for i in range(1,5,2):
  print(i)
```


### Day 6 - Functions, While loops


1. [Built-in Functions](https://docs.python.org/3/library/functions.html)

2. Define function and call function

```python
def function_name():     # define function
  do this

function_name()   # call function 
```

3. While loops
- statement after while is true, then do this

```python
while not end_of_game:     #end_of_game=False, then <not end_of_game> will be True
  do this

while True :       # infinite loop
  do this 
```


### [Day 7 - Project : Hanging Man](Day 7 Project -  Hanging Man/main.py)

