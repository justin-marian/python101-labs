class Cart:
    def __init__(self):
        """Initializes an empty shopping cart."""
        self.list_cart = []

    def add(self, new_product):
        """
        Adds a product to the shopping cart.

        Args:
            new_product (Product): The product to be added.
        """
        self.list_cart.append(new_product)

    def remove(self, product_name):
        """
        Removes a product from the shopping cart.

        Args:
            product_name (str): The name of the product to be removed.
        """
        self.list_cart = [product for product in self.list_cart if product.name != product_name]

    def view(self):
        """
        Returns the current list of products in the cart.

        Returns:
            list: The list of products in the cart.
        """
        return self.list_cart

    def cart_checkout(self):
        """
        Calculates the total price of all products in the cart and clears the cart.

        Returns:
            int: The total price of the products in the cart before checkout.
        """
        total = sum(product.price for product in self.list_cart)
        self.list_cart.clear()
        return total
