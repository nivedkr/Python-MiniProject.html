def add_item(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart
  
def create_cart(owner, discount=0):
    return {"owner": owner, "items": [], "discount": discount}

def add_to_cart(cart, name, price, qty=1):
    item = {"name": name, "price": price, "qty": qty}
    cart["items"].append(item)

def update_price(price_tuple, new_price):
   
    print("Attempting to modify tuple... Result: TypeError (Tuples are immutable)")

def calculate_total(cart):
    subtotal = sum(item['price'] * item['qty'] for item in cart["items"])
    total = subtotal * (1 - cart['discount'] / 100)
    return total

if __name__ == "__main__":
    cart1 = create_cart("Alice", discount=10)
    cart2 = create_cart("Bob")

    add_to_cart(cart1, "Laptop", 1000)
    add_to_cart(cart2, "Mouse", 25, qty=2)

    print(f"Alice's Total: ${calculate_total(cart1)}")
    print(f"Bob's Total: ${calculate_total(cart2)}")
- When you pass a list, you pass a reference. Modifying the list inside the 
  function changes the original object because they point to the same memory location.
"""
