import cart

class Store:
    def __init__(self, stock):
        """Initializes the store with a given stock and a dictionary for customer carts."""
        self.stock = stock
        self.customer_carts = {}

    def login(self, customer_id):
        """Creates a shopping cart for the customer upon login."""
        self.customer_carts[customer_id] = cart.Cart()

    def add_to_cart(self, customer_id, product_name):
        """
        Adds a product to the customer's cart and removes it from stock.
        
        Args:
            customer_id (int): The ID of the customer.
            product_name (str): The name of the product to add.
        """
        if customer_id not in self.customer_carts:
            return

        product = next((p for p in self.stock.view() if p.name == product_name), None)

        if product:
            self.customer_carts[customer_id].add(product)
            self.stock.remove(product_name)

    def remove_from_cart(self, customer_id, product_name):
        """
        Removes a product from the customer's cart and adds it back to stock.
        
        Args:
            customer_id (int): The ID of the customer.
            product_name (str): The name of the product to remove.
        """
        if customer_id not in self.customer_carts:
            return

        self.customer_carts[customer_id].remove(product_name)

        product = next((p for p in self.stock.view() if p.name == product_name), None)

        if product:
            self.stock.add(product)

    def view_cart(self, customer_id):
        """
        Returns a list of products (name and price) in the customer's cart.
        
        Args:
            customer_id (int): The ID of the customer.

        Returns:
            list of tuples (str, int): A list of (product_name, product_price) in the cart.
        """
        if customer_id not in self.customer_carts:
            return []

        return [(product.name, product.price) for product in self.customer_carts[customer_id].view()]

    def checkout(self, customer_id):
        """
        Processes the payment for the items in the customer's cart.
        
        Args:
            customer_id (int): The ID of the customer.

        Returns:
            int: The total price of the items in the cart.
        """
        if customer_id not in self.customer_carts:
            return 0

        return self.customer_carts[customer_id].cart_checkout()
