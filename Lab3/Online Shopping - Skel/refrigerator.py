import product

class Refrigerator(product.Product):
    def __init__(self, name, price, energy_label):
        product.Product.__init__(self, name, price)
        self.energy_label = energy_label

    def __str__(self):
        """
        Returns:
            * str:    un string ce va contine informatiile
                      specifice frigiderului (nume, energy label)
                    
        """
        return f"Enjoy fresh food with {self.name}, energy label {self.energy_label}."
