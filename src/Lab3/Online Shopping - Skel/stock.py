class Stock:
    def __init__(self, list_stock):
        """Initializes the stock with a given list of products."""
        self.list_stock = list_stock.copy()

    def add(self, new_product):
        """
        Adds a new product to the stock.
        
        Args:
            new_product (Product): The product to be added.
        """
        self.list_stock.append(new_product)

    def remove(self, product_name):
        """
        Removes a product from the stock by its name.
        
        Args:
            product_name (str): The name of the product to be removed.
        """
        self.list_stock = [product for product in self.list_stock if product.name != product_name]

    def view(self):
        """
        Returns the current list of products in stock.
        
        Returns:
            list[Product]: The list of available products.
        """
        return self.list_stock
