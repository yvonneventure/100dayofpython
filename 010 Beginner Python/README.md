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
