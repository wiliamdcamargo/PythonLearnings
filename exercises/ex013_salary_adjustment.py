# Create an algorithm that reads an employee's salary and displays their new salary with a 15% increase.
salary = float(input("Enter the employee's salary: C$"))
new_salary = salary + (salary * 15 / 100)
print("The employee who received C${:.2f} with a 15% increase will receive C${:.2f}.".format(salary, new_salary))
