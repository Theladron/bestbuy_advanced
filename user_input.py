def main_menu_input():
    """
    Gets user input for the main menu option, handles exceptions
    :return: user input as int
    """
    while True:
        try:
            menu_input = int(input("Please choose a number: "))
        except ValueError:
            print("Error. Please enter a number between 1-4.")
        else:
            if 1 <= menu_input <= 4:
                return menu_input
            else:
                print("Error. Please enter a number between 1-4.")


def order_item_input(product_list):
    """
    Gets input for the shop number that represents the chosen product
    or an empty string to cancel the order
    :param product_list: products in the shop as list
    :return: number that represents the item in the shop as int or empty string
    """
    while True:
        item_input = input("Which product # do you want? ")
        if not item_input:
            return item_input
        elif (item_input.isnumeric()
            and 1 <= int(item_input) <= len(product_list)):
            return int(item_input)
        else:
            print("Error. Please enter a valid product number or leave the input blank.")


def order_quantity_input():
    """
    Gets input for the quantity of the chosen product you want to buy
    or an empty string to cancel the order
    :return: quantity to buy as int or empty string
    """
    while True:
        quantity = input("What amount do you want? ")
        if not quantity:
            return quantity
        elif quantity.isnumeric():
            return int(quantity)
        else:
            print("Error. Please enter a number or leave the input blank.")
