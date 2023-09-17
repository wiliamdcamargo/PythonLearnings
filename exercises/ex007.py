# Create a program that reads a student's two grades, calculates and prints their average on the screen.
gradeOne = float(input("Enter the student's first grade: "))
gradeTwo = float(input("Enter the student's second grade: "))
average = (gradeOne + gradeTwo) / 2
print("The average between {:.1f} and {:.1f} is equal to {:.1f}.".format(gradeOne, gradeTwo, average))
