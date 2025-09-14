def add_sandwich(*stuff):
    print(f"making a sandwich with")
    for toppings in stuff:
        print(f"- {toppings}")


add_sandwich("bacon", "lettuce", "tomato")
add_sandwich("cheese", "lettuce", "tomato")
add_sandwich("turkey", "lettuce", "tomato")
