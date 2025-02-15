class Product:
    def __init__(self, name, price):
        """ 
        Initializes a product with a name and price.
        
        Args:
            name (str): The name of the product.
            price (int): The price of the product.
        """
        self.name = name
        self.price = price

    def __add__(self, other):
        """
        Overloads the '+' operator to return the sum of two product prices.
        
        Args:
            other (Product): The second product in the addition operation.
        
        Returns:
            int: The total price of both products.
        """
        return self.price + other.price
