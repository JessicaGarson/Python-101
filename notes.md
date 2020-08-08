# Python 101
Notes for the Python 101 class for generation data.

## Expressions
Expressions are basically math.
```python
2 + 2
5 - 3
3 * 7
22 / 7
2 + 3 * 20
```

Exponents look like this:
```python
2 ** 3
```

% is for modulus/remainder:
```python
22 % 8
```

// is for integer division/floored quotient:
```python
22 // 8
```

## Printing
The `print()` function will display the string value inside the parentheses on the screen. We are using the built in function of print which takes in a string as an argument.
```python
print('Hello World!')
```

## Variables
```python
name = 'Jess'
print(name)
```

The difference between these two.
```python
print(name)
print('name')
```
`print('name` prints the variable and `name` prints the variable.


## Running our first file
```bash
strings.py
```

## Quote styles
```python
print('hi')
print("hi")
print('hi")
```
You can use single or double quotes but only one option at a time.

## New line
There is a special character to use for a new line in a string.
```python
print('Hi, my name is: \nJessica')
```

## Tabs
There is also a special character to use for tabs
```python
print('Hi, my name is: \tJessica')
```

## Slicing
We can use slicing to get some elements of a string.
```python
name[0:]
name[0]
name[1]
name[2]
name[3]
name[4]
name[0:4]
name[0:]
name[0:1]
name[0:3]
name[-4]
name[-3]
name[-2]
name[-1]
name[-4:-1]
```

## String formatting
One of my favorite things about code is there are multiple ways to do this . `.format` is one method, you can also use f strings or `%s`.

```python
hi = 'Hi my name is {}'.format(name)
print(hi)
age = 35
hi_with_age = 'hi my name {} and I am {} years old.'.format(name, age)
print(hi_with_age)
```

## A simple Tweet length calculator
```python
tweet = 'My python class is so fun with @JessicaGarson as my instructor'
print(len(tweet))
print('That tweet is {} characters and you have {} remaining characters'.format(len(tweet), 240- len(tweet)))
```

## We can also do math with strings
```python
print('Jess' + 'Class')
print('Jess' * 3)
```
## String methods
Works like Ctrl-F in most programs but you get back the index(slice) of where the thing you are looking for is located.

```python
email = 'jessica.garson@gmail.com'
print(email.find('@'))
```

Upper and lower turns your string into all upper case or or all lower. This is very helpful for validation.
```python
print(twitter.upper())
print(twitter.lower())
```

## Count
```python
wonderwall = '''Today is gonna be the day that they're gonna throw it back to you by now you should've somehow realized what you gotta do
I don't believe that anybody feels the way I do, about you now. Backbeat, the word was on the street that the fire in your heart is out I'm sure you've heard it all before but you never really had a doubt I don't believe that anybody feels the way I do about you now.'''
print(wonderwall.count('you'))
```

## Input
You can have your program ask you questions.
```python
question = input("What's your name? ")
print(question)
```

## Conditionals
We use conditionals to compare two things and we can have Python help us out by evaluating what is true or false.

```python
1 == 2
2 != 3
5 > 4
3 < 100
4 >= 92
4 <= 5
```

## If statement
An if statement evaluates whether a statement is true or false, and run code only in the case that the statement is true.

```
space = 15
if space < 20:
  print('We still have spaces left')
```

## Else
A catchall if none of the conditions meet.
```python
space = 21

if space < 20:
  print('We still have spaces left')
else:
  print('Sorry, we are full')
```

## Elif
If there is another condition that is met than do something else.

```python
space = 19

if space < 20:
  print('We still have space left')
elif space == 20:
  print('We are just a capacity')
elif space >= 19:
  print('We still have space left')
else:
  print('Sorry, we are full')
```

## Functions
Functions help us repeat ourselves less. They are reusable bits of code that we can use as many times aw want.

```python
def hey():
    print("Hey! Good to see you!")
    name = input("What's your name?\n")
    print("Oh hello {}!".format(name))
hey()

print("Nice to meet you! Have a good day")
```
## Return values
Allows you to set a value to return.

```python
def name():
    return input("What's your name?\n")


my_name = name()
print("Oh hello {}!".format(name))
```
