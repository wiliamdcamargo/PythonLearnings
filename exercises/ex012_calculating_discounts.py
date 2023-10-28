# Create an algorithm that reads the price of a product and displays its new price with a 5% discount on the screen.
product_price = float(input("Enter the price of the product: C$"))
new_product_price = product_price - (product_price * (5 / 100))
print("The product that used to cost C${} in the promotion with 5% discount it will cost C${:.2f}.".format(product_price, new_product_price))
