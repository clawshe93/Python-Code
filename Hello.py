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

name = input("What is your name? ")
color = input ("What is your favorite color? ")
age = input("How old are you today? ")

#print ("Hello, " + name + "!" + " I see your favorite color is " + color + " and you are " + age + " years old today.")

#print (name, end =" ")
#print ("is " + str(age) + " years old", end =" ")
#print ("and loves the color " + color +".", end =" ")

print(name, 'is', age, 'years old and loves the color', color + '.', sep=" ")