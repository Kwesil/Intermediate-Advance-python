class Item:
    def __init__(self, name: str, price: float, quantity: int): # constructor
        """This is the constructor method that initializes the instance variables."""

        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"
        
        # Assign to self object variables
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price *  self

item1 = Item("Phone", 100, 5)
"""item1.name = 'Phone'
item1_price = 100
item1_quantity = 5
#item_price_total = item1_price * item1_quantity
# print(item1.calculate_total_price(item1.price, item1.quantity))"""

item2 = Item("Laptop", 100, 5)
item2.has_numpad = False
"""item2.name = "Laptop"
item2.price = 1000
item2.quantity = 3
# print(item2.calculate_total_price(item2.price, item2.quantity))"""

