import products
import promotions
import store
import user_input


def show_current_stock(shop):
    """
    Gets total quantity of all products in the shop
    :param shop: Store class, loaded with products from Product class
    """
    print(shop.get_total_quantity())
    print("----------")


def show_products(shop):
    """
    Gets all products currently in the shop
    :param shop: Store class, loaded with products from Product class
    """
    print("----------")
    product_list = shop.get_all_products()
    for index, product in enumerate(product_list):
        print(f"{index + 1}. {product}")
    print("----------")


def make_order(shop):
    """
    Creates a list of tuples with product and quantity from repeated user inputs,
    calls the order from the list
    :param shop: Store class, loaded with products from Product class
    """
    show_products(shop)
    product_list = shop.get_all_products()
    print("When you want to finish order, enter empty text.")
    order_list = []
    while True:
        item = user_input.order_item_input(product_list)
        quantity = user_input.order_quantity_input()
        if isinstance(item and quantity, int):
            order_list.append((product_list[item - 1], quantity))
        else:
            break
    if order_list:
        print(shop.order(order_list))


def start(shop):
    """
    Shows the menu functions, gets user input and calls the functions
    interacting with the shop, ends the program if shop is empty
    :param shop: Store class, loaded with products from Product class
    """
    menu_funct = {1: show_products,
                  2: show_current_stock,
                  3: make_order,
                  }
    while True:

        print("""
    Store Menu
    ----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit""")
        if not shop.get_all_products():
            print("\nThe shop does not have any products left. Thank you for"
                  " your purchase and have a nice day!")
            exit()
        menu_choice = user_input.main_menu_input()
        if menu_choice == 4:
            exit()
        else:
            menu_funct[menu_choice](shop)


def main():
    """
    Creates a list of product instances, adds promotions
    and starts the menu interface, handles exceptions
    """
    try:
        # setup initial stock of inventory
        product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    products.NonStockedProduct("Windows License", price=125),
                    products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                    ]

        # Create promotion catalog
        second_half_price = promotions.SecondHalfPrice("Second Half price!")
        third_one_free = promotions.ThirdOneFree("Third One Free!")
        thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

        # Add promotions to products
        product_list[0].promotion = second_half_price
        product_list[0].promotion = third_one_free
        product_list[1].promotion = third_one_free
        product_list[4].promotion = thirty_percent
        product_list[0].promotion = thirty_percent
        best_buy = store.Store(product_list)

    except ValueError as error:
        print(f"Error with the input values: {error}")
    except TypeError as error:
        print(f"Error with the input type: {error}")
    except NameError as error:
        print(f"Error catching name: {error}")
    else:
        start(best_buy)


if __name__ == "__main__":
    main()
