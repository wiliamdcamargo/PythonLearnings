# Create an algorithm that reads a number and displays its double, triple and, squere root on the screen.
number = int(input('Enter a number: '))
print('The double of {} is equal to {}.'.format(number, number * 2))
print('The triple of {} is equal to {}.'.format(number, number * 3))
print('The square root of {} is equal to {:.2f}.'.format(number, number ** 0.5))
