print("********** WELCOME **********")

customer_name = input("\nWhat is your name? ")

print("""Today's menu
1. Chocolate Cake
2. Oreo Cake
3. Strawberry Cake
4. Black forest cake""")

cake_price = 400

cake_flavour = input("Which cake flavour you want? : ")

cake_quantity = input("\nHow many " + cake_flavour + " you want? : ")

total_bill = cake_price * int(cake_quantity)

print("\nYour total bill is " + str(total_bill))

print("\nThanks for coming! Please visit again")
