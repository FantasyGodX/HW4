import itertools

def addNumbers(x, y):
    return x + y

    print (x + y)
    return 0

add_Lambda = lambda x, y: x + y

def join_words(*words):
    print(" ".join(words))

join_lambda = lambda *words: " ".join(words)


def countdown(x):
    if x == 0:
        print(0)
    else:
        print(x)
        countdown(x-1)

def greet(name):
    print("Hello " + name + ". Welcome to my python program.\n")

def repeat_Phrase(phrase , num = 2):
    for i in range(num):
        print(phrase)

def apply_Function(func , value):
    return func(value)


def safe_divide(a , b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Can't divide by zero"

def parse_int(value):
    try:
        return int(value)
    except ValueError:
        return "Error: Please enter a number"

def safe_divide1(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Can't divide by zero"
    finally:
        print("Division attempted")




addNumbers(3,5)
add_Lambda(3, 5)
join_words("Hello", "world", "!")
print(join_lambda("Hello", "world", "!"))
print(countdown(5))
greet("Alice")
repeat_Phrase("Hi ")
print("\n")
repeat_Phrase("Hi " , 3)
print(apply_Function(lambda x: x.upper(), "hello"))
print(safe_divide(16,4))
print(safe_divide(7,0))
print(parse_int("3.14"))
safe_divide1(4,0)

I = iter([5,4,3,2,1])
for i in range(5):
    print(next(I))

words = ['apple' , 'banana' , 'orange' , 'pear' ]

upper_words = (word.upper() for word in words)

for word in upper_words:
    print(word)

class Countdown:
    def __init__(self, start):
        self.current = start  # Initialize countdown start value

    def __iter__(self):
        return self  # The iterator object itself

    def __next__(self):
        if self.current < 0:  # Stop when reaching below zero
            raise StopIteration
        value = self.current  # Store the current value
        self.current -= 1  # Decrease by 1
        return value  # Return the current countdown value

print("\n")

x = Countdown(10)
print(next(x))
print(next(x))
print("\n")

colors = ["red" , "blue" , "green"]
color_cycle = itertools.cycle(colors)

for _ in range(6):
    print(next(color_cycle))

