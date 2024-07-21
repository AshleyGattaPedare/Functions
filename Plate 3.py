# Define a function called apply_discount that applies a 25% discount to sushi items with a price above $4.00.
# You will need to keep the first two functions to make the ordering system functional - jump down to line 40 for the first step.

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

def calculate_total(items_ordered):
    sushi_prices = {
        "Salmon Nigiri": 3.50,
        "Tuna Roll": 4.25,
        "Eel Nigiri": 4.75
    }
    total_cost = 0
    for item in items_ordered:
        total_cost += sushi_prices.get(item, 0)
    print(f"Total cost: ${total_cost:.2f}")



# Step 1: define a function called 'apply_discount(items_ordered)'

def 
    sushi_prices = {
        "Salmon Nigiri": 3.50,
        "Tuna Roll": 4.25,
        "Eel Nigiri": 4.75
    }


# Step 2:  On line 55, make discounted_prices an empty dictionary.

# Step 3: Add to the code from line 57 to use a for loop and an if/else statement to iterate through the sushi available and apply a 25% discount to those that are above $4.00.


    discounted_prices = 

    for item in :
        if sushi_prices[item] 
            discounted_prices[item] = sushi_prices[item] * 
        else:
            discounted_prices[item] = sushi_prices[item]
    
    total_cost_with_discount = 0
    for item in items_ordered:
        total_cost_with_discount += discounted_prices.get(item, 0)
    
    print(f"Total cost with discount: ${total_cost_with_discount:.2f}")

ordered_items = sushi_menu()
calculate_total(ordered_items)
apply_discount(ordered_items)
