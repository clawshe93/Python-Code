my_str = "Yo " * 4 + "Come check this crazy "

my_str = my_str + "flow!"

print (my_str)

print (4.5e9)
print (2/3 + 4/3)

first = "Ross"
last = "Taylor"
full_name = first + " " + last
print ("Hello " + full_name + "! You just delved into python.")

middle_ball = "Squirtle"
left_ball = "Bulbasaur"
right_ball = "Charmander"

print ("You can choose " + left_ball + ", " + middle_ball + " or " + right_ball + " as your starter companion!" )

#name = input("What is your name? ")
#color = input ("What is your favorite color? ")
#age = input("How old are you today? ")

#print ("Hello, " + name + "!" + " I see your favorite color is " + color + " and you are " + age + " years old today.")

#print (name, end =" ")
#print ("is " + str(age) + " years old", end =" ")
#print ("and loves the color " + color +".", end =" ")

#print(name, 'is', age, 'years old and loves the color', color + '.', sep=" ")

#Indexing simple example
test_str = 'testing'
print(test_str[len (test_str) - 1])


#Splicing simple example
print(test_str[0:2])
print(test_str[3:5])
print(test_str[2:])
print(test_str[1:6:2])
print(test_str[::-1])

#Lists and other associated things

my_list = [1, 2, 3, 4, 5, 6, 7, 8]

print (my_list)

print (my_list[1::2])
print (my_list[0::2])

my_list[0:2] = ['a', 'b']

print (my_list)

del my_list[1]

print (my_list)

#Matrices and Cubes

my_matrix = [[1, 2, 3], [4, 5, 6]]
row_count = len(my_matrix)
column_count = len(my_matrix[0])

print(my_matrix[0][1])
print(my_matrix[1][1])
print(my_matrix[1][2])

#Tuples

point = (2.0, 3.0)
point_3d = point + (4.0,)

print (point)

x, y, z = point_3d

print (x)
print (y)
print (z)

print("My name is: %s %s" % ("Keith", "Thmpson"))

person = ('Chris Lawshe', 29, '314-xxx-xxxx')
person2 = ('Mike Ross', 42, '212-xxx-xxxx')
print (person2[0])

my_tuple = (my_list, 1)
print (my_tuple)
other_list = [1, 2, my_tuple]
print (other_list)

my_list.append(1)
print (my_tuple)
print (other_list)

#Dictionaries

ages = {'Chris': 59, 'Joy': 25, 'Strick': 78}
print (ages)

ages['Kayla'] = 21

print (ages)

ages ['Chris'] = 85

print (ages)

del ages['Joy']

print (ages)

print ('Joy' in ages)
print ('Chris' in ages)

weights = dict(kevin = 160, bob = 240, kayla = 125)
print (weights)

colors = dict([('Kevin', 'Blue'),('Bob', 'Green'),('Kayla', 'Red')])
print (colors)

print (ages.keys())

print (ages.values())

print (ages.items())

#Strings

print (ord('\u2122'))
print ('\u2122')

print (chr(8482))

print ("This".lower())
new_str = "tEsTinG"

print (new_str.lower())
print (new_str.upper())
print (new_str.capitalize())

print ("This is a multiword string".title())

print ("Chris@example.com" == "chris@example.com")
print ("Chris@example.com".lower() == "chris@example.com")

print (new_str.isascii())
print (new_str.islower())
print (new_str.title().istitle())

print ("123".isdecimal())
print ("123.0".isdecimal())

print ("123".isdigit())
print ("123.0".isdigit())

print ("123".isnumeric())
print ("123.0".isnumeric())

print ("A, B, C are alphabetical characters: ", "abc".isalpha())
print ("1, 2, 3 are alphabetical characters: ", "123".isalpha())

print ("1, 2, 3 are alpha-numeric characters: ", "123".isalnum())
print ("1, 2, A, B are alpha-numeric characters: ", "12ab".isalnum())

print ("1bear".isidentifier())
print ("word".isidentifier())

print("This is printable.".isprintable())
print("This is printable.\n".isprintable())

phrase = "This is a simple phrase"
words = phrase.split()

print (words)

url = "https://example.com/users/jimmy"
user = url.split('/')[-1]

print (user)

print(", ".join(words))

lines = ['First line', 'Second line', 'Third line']

output = '\n'.join(lines)
print(output)

template = ("Hello, my name is {}, and I really enjoy {}. Have a nice day!")

print (template.format('Chris', 'Python'))

print (template.format('Chris', 'Python', 'Gee-Willakers!'))

template2 = ("Hello, my name is {0}, and I really enjoy {1}. Have a nice day! - {0}".format('Chris', 'Python'))

print (template2)

#Conditionals

if 'a' < 'b':
    print ("Condition was true")
if 'b' < 'a':
    print ("Condition was true")
if False:
    print ("Was true")
else:
    print ("Was false")
if True:
    print ("Was true")
else: 
    print ("Was false")

if 'b' < 'a':
    print ("This is true")
elif 'c' < 'd':
    print("Second condition is true")
else:
    print ("No condition was true")
    
#name = input("What is your name? ")

#if len(name) >= 6:
#    print ("Your name is long!")
#elif len(name) == 5:
#    print ("Your name is 5 characters.")
#elif len(name) >= 4:
#    print("Your name is 4 or more characters.")
#else:
#    print("Your name is short.")

#name2 = "Keith"
#if name2 == "Kevin":
#    print("Hello Kevin")
#else:
#    pass

value = int(input("Enter an integer value: "))

if value % 5 == 0 and value % 3 == 0 and value % 2 == 0:
    print("FizzBuzzCuzz")
elif value % 5 == 0 and value % 3 == 0:
    print("FizzBuzz")
elif value % 5 == 0 and value % 2 == 0:
    print("FizzCuzz")
elif value % 3 == 0 and value % 2 == 0:
    print("BuzzCuzz")
elif value % 5 == 0:
    print("Fizz")
elif value % 3 == 0:
    print("Buzz")
elif value % 2 == 0:
    print("Cuzz")
else:
    print(value)
    
    
#Loops
    
colors = ['red', 'blue', 'orange', 'green', 'yellow']
for color in colors:
    print(color)

point = (1, 2, 3)
for value in point:
    print(value)
    
new_ages = {'kevin': 59, 'bob': 40, 'kayla': 21}
for key in new_ages:
    print(key)
for key, value in new_ages.items():
    print(key, value)
    
counter = 1
while counter <=25:
    if counter % 4 == 0:
        print(counter)
    counter += 1

count = 1
while count < 10:
    if count % 2 == 0:
        break
    print(f"We're conting odd numbers: {count}")
    count += 1
    
for color in colors:
    if color == 'blue':
        continue
    if color == 'red':
        break
    print(color)
    
while count <= 4:
    print(count)
    count += 1
else:
    print ("While loop completed")
    
for i in [1, 2, 3, 4, 5]:
    print(i)
else:
    print("For loop completed")

for color in colors:
    if color == 'orange':
        print("Orange is in the list.")
        break
else:
    print("Orange is not in the list.")
    
my_range = range(10)
print (list(range(1, 14, 2)))

while count <= 4:
    print("Looping")
    count += 1
for _ in range(4):
    print("Looping")

uppercase_colors = [color.upper() for color in colors]
print(uppercase_colors)

warm_colors = [color for color in colors if color in ['red', 'orange', 'yellow']]
print(warm_colors)

#Functions

def print_something(something):
    pass
def print_name(name):
    print(f"Name is {name}")

print (print_name('Chris'))

output = print_name("Chris")

def add_two(num):
    return num + 2

result = add_two(3)
print(result)

def add(num1, num2):
    return num1 + num2
print (add(1, 5))

def contact_card(name, age, car_model):
    return f"{name} is {age} and drives a {car_model}"

print(contact_card("Chris", 29, "Toyota Camry"))

print(contact_card(age = 29, car_model = "Toyota Camry", name = "Chris"))

def can_drive(age, driving_age = 16):
    return age >= driving_age
print (can_drive(15))

#Generators

def gen_range(stop, start=1, step=1):
    num = start
    while  num <= stop:
        yield num
        num += step

generator = gen_range(10)

print(list(generator))

def gen_fib():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a
        
fib = gen_fib()

print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))

prit(list(fib))
