#recieve celsius from user
celsius = input("enter the temperature in celsius")
#Convert to integer
celsius = int(celsius)

#Formula (0°C × 9/5) + 32
Farenheit = (celsius * 9/5) + 32
#convert to float
Farenheit = float(Farenheit)

print("The temperature in farenheit is " + str(Farenheit))