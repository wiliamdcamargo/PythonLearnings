# Create a program that reads the amount of money a person has in their wallet
# and displays on the screen the amount of Canadian dollars they can buy.
amount_brl = float(input("How much money do you have in your wallet? R$"))
amount_cad = amount_brl / 3.61451
print("With R${:.2f} you can buy C${:.2f} today.".format(amount_brl, amount_cad))
