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

print(my_matrix[0] [1])
print(my_matrix[1][1])
print(my_matrix[1][2])