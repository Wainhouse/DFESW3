
# (C*1.8) + 32 = F

# cels = 0

# faren = (cels * 18) + 32

# # print("%.2f Celcius = %.2f Fahrenheit" % (cels, faren))

# temperature = float(input("Please enter a temperature, followed by your chosen unit, C or F!"))

# c = temperature.find('C')

# f = temperature.find('F')

# if temperature.find == f:
#     print

# This is correct!!!!!!!!
unit = (str(input("Which would you like to convert, C or F?")))
temperature = int(input("Please enter a temperature!"))

if unit == 'F':
    fahrenheit = (temperature * 1.8) + 32
    print(fahrenheit)

elif unit == 'C':
    celcius = (temperature / 1.8) - 32
    print(celcius)
else:
    print("Run again and enter a testable value")
