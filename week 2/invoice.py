# invoice
# Ask for the name of a product sold
item_name = input('What is the product name? ')
# ask how many were sold
items_sold = int(input('How many items were sold? '))
# ask for the price of one item
unit_price = float(input("how much does one item cost? "))
# do the math to figure out the total price
total = items_sold * unit_price

# print a neat invoice with all the data in
print()
print(item_name + ' Sales')
print('Quantity sold: ' + str(items_sold))
print('Unit price: $' + str(unit_price))
print('Total: $' + str(total))
