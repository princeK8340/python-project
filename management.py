# definr cafe menu
menu = {
    'pizza':40,
    'pasta':50,
    'coffee':60,
    'tea':30,
    'nudels':55,

}

#greet
print('''Welcome to Cafe!!
     how can i help you''')
print("pizza : Rs40\n Pasta : Rs50\n coffee : Rs60\n tea : Rs30\n nudels :Rs55\n")

order_total=0
item_1= input("Enter the name of order you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item{item_1} has been added in your order. ")

else:
    print(f"order item{item_1} is not avavilable yet!!")

another_order = input("Do you want order to another order ?(Yes/no)")
if another_order == "Yes":
   item_2 = input("Enter the nsme of second item = ")
   if item_2 in menu:
      order_total += menu[item_2]
      print(f"item{item_2} has been added in your order.")
   else:
      print(f"order item {item_2} is not avavilable.")

print(f"Total amount to pay {order_total}")
      
     

