# The goal of this task is to create a function called sushi_menu that contains a dictionary of sushi types and their prices. The function should take an order from the customer and add it to a list called items_ordered.

# Step 1: The function sushi_menu has been defined and a dictionary of products and their prices added for you. Add at least two items to the dictionary that you find delicious.


def sushi_menu():
    sushi_prices = {
        "Salmon Nigiri": 3.50,
        "Tuna Roll": 4.25,
        "Eel Nigiri": 4.75
    }
    

# Step 2: On line 16, create an empty list called 'items_ordered.'

  
  
# Step 3: Print the menu (items and their price).
    print("Sushi Menu:")
    for 
        print(f"{item}: ${price:.2f}")


# Step 4: Taking the order from the customer has been done for you below. Use a return on line 37 to exit the function and add the items to the list.
  

  while True:
        order = input("\nEnter the sushi item you want to order (or type 'done' to finish): ")
        if order.lower() == 'done':
            break
        elif order in sushi_prices:
            items_ordered.append(order)
            print(f"{order} added to your order.")
        else:
            print("Sorry, that item is not on the menu.")

    return 

# This calls the function and stores the result (the items ordered from the menu).
ordered_items = sushi_menu()
