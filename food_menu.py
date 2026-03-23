choice = int(input("1.Samosa 2.Chowmein 3.Burger 4.Patties 5.Manchurian: "))
qty = int(input("Enter quantity: "))

if choice == 1:
    total = 20 * qty
elif choice == 2:
    total = 50 * qty
elif choice == 3:
    total = 60 * qty
elif choice == 4:
    total = 25 * qty
elif choice == 5:
    total = 70 * qty
else:
    total = 0

print("Total Bill: ₹", total)