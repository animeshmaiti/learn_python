class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def add_product(self, product, quantity):
        if product.product_id in self.cart:
            self.cart[product.product_id]['quantity'] += quantity
        else:
            self.cart[product.product_id] = {'product': product, 'quantity': quantity}

    def remove_product(self, product_id, quantity):
        if product_id in self.cart:
            if self.cart[product_id]['quantity'] <= quantity:
                del self.cart[product_id]
            else:
                self.cart[product_id]['quantity'] -= quantity

    def view_cart(self):
        cart_info = {}
        for item in self.cart.values():
            cart_info[item['product'].name] = item['quantity']
        return cart_info

    def calculate_total(self):
        total_cost = 0
        for item in self.cart.values():
            total_cost += item['product'].price * item['quantity']
        return total_cost

    def apply_discount(self, discount):
        for item in self.cart.values():
            item['product'].price -= item['product'].price * discount

# Example usage:
product1 = Product(1, 'Laptop', 1000, 5)
product2 = Product(2, 'Mouse', 20, 10)

cart = ShoppingCart()
cart.add_product(product1, 2)
cart.add_product(product2, 3)

print("Initial Cart:")
print(cart.view_cart())
print("Total Cost:", cart.calculate_total())

cart.remove_product(1, 1)
print("\nAfter removing one laptop:")
print(cart.view_cart())
print("Total Cost:", cart.calculate_total())

cart.apply_discount(0.1)  # Applying 10% discount
print("\nAfter applying 10% discount:")
print(cart.view_cart())
print("Total Cost:", cart.calculate_total())
