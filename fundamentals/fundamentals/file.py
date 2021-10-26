num1 = 42                     #variable declaration,initilize numbers
num2 = 2.3                    #variable declaration,initilize numbers
boolean = True                 #variable declaration,initilize boolean
string = 'Hello World'         #variable declaration,initilize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']   # initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana')      # initialize tuple
print(type(fruit))                                 # print type of variable
print(pizza_toppings[1])                           # print list index value 1 
pizza_toppings.append('Mushrooms')                 # add the value in list
print(person['name'])                              # print dictionary key value
person['name'] = 'George'                          # change the key value
person['eye_color'] = 'blue'                       # add new key value in dictionary
print(fruit[2])                                   # print tuple index value2

if num1 > 45:                                     # conditional statement
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5):             #  for loop
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5):                # while loop
    print(x)
    x += 1

pizza_toppings.pop()         # remove the value from end
pizza_toppings.pop(1)        # remove value index 1

print(person)
person.pop('eye_color')      # remove key value eye_color from dictionary 
print(person)

for topping in pizza_toppings:       #for loop
    if topping == 'Pepperoni':        # conditional statement
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():           # function definition
    for num in range(10):
        print('Hello')

print_hello_ten_times()               # function calling

def print_hello_x_times(x):           # function definition
    for num in range(x):              # for loop
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):   # function definition
    for num in range(x):                  # for loop
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
num3 = 72                   # variable declearation , initialinze number 
print(num3)                  # print number
#fruit[0] = 'cranberry'        # TypeError: 'tuple' object does not support item assignment
#print(person['favorite_team'])  # KeyError: 'favorite_team'
#print(pizza_toppings[7])             # IndexError: list index out of range
print(boolean)                        # print boolean value
fruit.append('raspberry')             # AttributeError: 'tuple' object has no attribute 'append'
fruit.pop(1)                          #AttributeError: 'tuple' object has no attribute 'pop'