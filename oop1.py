class Item:
    pay_rate =  0.8 # The pay rate after 20% discount
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
    
    def apply_discount(self):
        """This method applies the discount to the price."""
        self.price = self.price * self.pay_rate

item1 = Item("Phone", 100, 5)
item1.apply_discount()  # Applying discount to item1
print(item1.price)

item2 = Item("Laptop", 100, 5)
item2.has_numpad = False
item2.pay_rate = 0.7  # Overriding the class variable for this instance
item2.apply_discount()  # Applying discount to item2
print(item2.price)  # Price after discount for item2


