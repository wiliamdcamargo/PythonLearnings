# Create a program that reads the width and height of a wall in meters.
# Calculate its area and the amount of paint needed to paint it, knowing that each liter of paint paints an area of 2m².
width = float(input("Enter the width of the wall: "))
height = float(input("Enter the height of the wall: "))
area = width * height
amount_paint = area / 2
print("Your wall has a dimension of {}x{} and its area is of {}m².".format(width, height, area))
print("To paint this wall, you will need {}l of paint.".format(amount_paint))
