
#Python implementation goes here

fahrenheit = float(input("What temperature (in Fahrenheit) would you like converted to celcius?"))

celcius = (fahrenheit  - 32) * 5 / 9

print(fahrenheit, 'F is', round(celcius, 2), 'C.')