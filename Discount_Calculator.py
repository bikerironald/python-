
# Discount Calculator with elif
purchase_amount  = float(input("Enter the price of the item: "))
if purchase_amount <= 1000:
    discount = 0
    print("No discount applicable.")
elif purchase_amount <= 5000:
    discount = purchase_amount * 0.1
    print(f"Discount is 10%: {discount}")
else:
    discount = 0
final_price = purchase_amount * (1 - discount)
print("Final price after discount: $" + str(final_price))