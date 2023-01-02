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




