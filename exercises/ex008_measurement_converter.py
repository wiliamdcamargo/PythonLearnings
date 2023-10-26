# Write a program that reads a value in meters and displays it converted into:
# Kilometer, Hectometer, Decameter, Decimeter, Centimeter, and Millimiter.
distance = int(input("Enter a distance in meters: "))
print("The measurement of {}m corresponds to:".format(distance))
print("{}km".format(distance / 1000))
print("{}hm".format(distance / 100))
print("{}dam".format(distance / 10))
print("{}dm".format(distance * 10))
print("{}cm".format(distance * 100))
print("{}mm".format(distance * 1000))
