# *Online Shopping*

## Requirement

Since it is known that mathematics is the favorite subject of students, this task will propose to implement a complex number calculation system.
Thus, in order to deepen object-oriented programming, the following methods are desired to be implemented inside the Complex() class:
>On the occasion of Black Friday, a newly established online home appliance store has prepared unbeatable discounts and needs help with the logistical side of the site. Being at the beginning, the store has a stock consisting of only two types of products: phones and refrigerators. Your task is to implement the necessary functionalities to make sure that the site will work properly.
>For example, the store will have the following functionalities:
>User side:

* Once a user logs in, he receives a unique customer_id and can start shopping(login(self, customer_id));
* Can add a product to his cart (shopping cart) as long as it is in stock. A product added to the cart will disappear from stock ( add_to_cart(self, customer_id, product_name));
* There is also a situation where the buyer can change his mind, he no longer wants a product already added to the cart. After a product has been removed from the cart, it returns to stock (remove_from_cart(self, customer_id, product_name));
* The user can see the products added to the cart and their price, and if not yet registered, return an empty list (view_cart(self, customer_id)) Finally, pay for the products, that is, return the total amount of prices in the user's cart, and if the user is not registered, the value 0 will be returned (checkout(self, customer_id))
Admin side: Implement a method for the site administrator to add products to stock, a dual-role method, also used when the user has removed a product from his cart (add(self, new_product))

>It is worth noting that the store will not work without the entities behind it (the cart, the products, the stock, etc.). Complete the necessary methods (TODO) to ensure that the store will function at the level of customer expectations.

## Product Class

```text
TODO 1:
* complete the constructor of the Product class

TODO 2:
* complete the overloading of the "+" operator
* will return the sum of the prices of the two products
```

## Phone Class

```text
TODO:
* overload the str method
```

## Refrigerator Class

```text
TODO:
* overload the str method
```

## Stock Class

```text
TODO 1:
* add a new product to the stock

TODO 2:
* delete the product given as a parameter from the store's stock

TODO 3:
* return the current stock

```

## Cart Class

```text
TODO 1:
* add a product to the shopping list list_cart

TODO 2:
* delete the product from the shopping list list_card

TODO 3:
* calculate the sum of the prices of all products in the cart
* empty cart (after cart_checkout, the cart will be empty)
```

## Store Class

```text
TODO 1:
* add a product to the cart of a buyer with the given id
** if the buyer is not logged in (his id is not in the list), the operation will not be performed (the cart remains unchanged)
* once a product has been added to the cart, it is deleted from the stock

TODO 2:
* delete a product from the buyer's cart
** if the buyer is not logged in (his id is not in the list), the operation will not be performed (the cart remains unchanged)
* the product will be added back to the store's stock

TODO 3:
* return the list of products (name and price) in the cart

TODO 4:
* return the price of the products in the cart
```

## Run | Testing

For testing, you can run the script directly from the IDE or you can run the command in the terminal:

```bash
./checker.py
```

If you cannot run this script due to permissions, use the following command first:

```bash
sudo chmod 700 checker.py
```
