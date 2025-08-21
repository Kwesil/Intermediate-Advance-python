# Class and static methods
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

    @classmethod
    def instantiate_from_csv(cls):

        """This method reads from a CSV file and creates instances of Item."""
        import csv
        with open(r'C:\Users\Nwabike\Desktop\NewTech\OOP\item.csv', 'r') as file:
            reader = csv.DictReader(file)
            items = list(reader)

            for item in items:
                Item(
                    name=item.get('name'),
                    price=int(item.get('price')),
                    quantity=(item.get('quantity'))
                )

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


Item.instantiate_from_csv()