# attributes
class Item:
    pay_rate = 0.8  # The pay rate after 20% discount
    all = []  # This is a class variable that will hold all instances of Item

    def __init__(self, name: str, price: float, quantity: int):  # constructor
        """This is the constructor method that initializes the instance variables."""

        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"
        
        # Assign to self object variables
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        """This method applies the discount to the price."""
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5) 

# for instance in Item.all:
#     instance.apply_discount()
#     print(f"{instance.name} - Price after discount: {instance.price}, Total price: {instance.calculate_total_price()}")

print(Item.all)