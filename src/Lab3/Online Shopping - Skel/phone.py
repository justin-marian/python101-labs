import product

class Phone(product.Product):
    def __init__(self, name, price, ram, cpu):
        """
        Initializes a Phone object, inheriting from the Product class.

        Args:
            name (str): The name of the phone.
            price (int): The price of the phone.
            ram (str): The amount of RAM in the phone.
            cpu (str): The type of CPU used in the phone.
        """
        super().__init__(name, price)
        self.ram = ram
        self.cpu = cpu

    def __str__(self):
        """
        Returns a formatted string containing details about the phone.

        Returns:
            str: A description of the phone, including its name, CPU, and RAM.
        """
        return f"The new {self.name} offers an unforgettable experience, featuring a {self.cpu} CPU and {self.ram} RAM."
