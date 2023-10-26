# Create a program that reads a student's two grades, calculates and prints their average on the screen.
grade_one = float(input("Enter the student's first grade: "))
grade_two = float(input("Enter the student's second grade: "))
average = (grade_one + grade_two) / 2
print("The average between {:.1f} and {:.1f} is equal to {:.1f}.".format(grade_one, grade_two, average))
