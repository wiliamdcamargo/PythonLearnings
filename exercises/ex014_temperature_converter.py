# Write a program that reads a temperature in °C and converts it into °F.
temperature_celsius = float(input("Enter the temperature in °C: "))
temperature_fahrenheit = (temperature_celsius * 9 / 5) + 32
print("The temperature of {}°C corresponds to {}°F!".format(temperature_celsius, temperature_fahrenheit))
