# Write a program that asks how many kilometers a rental car has traveled and the number of days it has been rented for.
# Calculate the price to be paid, given that the car costs C$60 per day and C$0.15 per km driven.
rented_days = int(input("How many days was the car rented for? "))
kilometers_driven = int(input("How many kilometers were driven? "))
total_cost = (rented_days * 60) + (kilometers_driven * 0.15)
print("The total to be paid is C$ {:.2f}.".format(total_cost))