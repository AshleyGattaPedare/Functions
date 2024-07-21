# Now we are going to take the items ordered, store them in a list and calculate the total price. Part of this has been completed for you. Jump to line 27.

def sushi_menu():
    sushi_prices = {
        "Salmon Nigiri": 3.50,
        "Tuna Roll": 4.25,
        "Eel Nigiri": 4.75
    }
    items_ordered = []
    print("Sushi Menu:")
    for item, price in sushi_prices.items():
        print(f"{item}: ${price:.2f}")
    
    while True:
        order = input("\nEnter the sushi item you want to order (or type 'done' to finish): ")
        if order.lower() == 'done':
            break
        elif order in sushi_prices:
            items_ordered.append(order)
            print(f"{order} added to your order.")
        else:
            print("Sorry, that item is not on the menu.")
    
    return items_ordered


# Step 1: define a function called 'calculate_total' using the list 'items_ordered.'

def calculate_total(items_ordered):
    sushi_prices = {
        "Salmon Nigiri": 3.50,
        "Tuna Roll": 4.25,
        "Eel Nigiri": 4.75
    }
    total_cost = 0


# Step 2: In line 42, use a 'for' loop to iterate through the items ordered.

# Step 3: Use a print statement in line 44 to print the total cost of the order.
  
    for 
        total_cost += sushi_prices.get(item, 0)
    print()


# Step 4: Finish calling both functions (ordered_items and calculate_total) to get the program to work. 

ordered_items = 
calculate_total(

