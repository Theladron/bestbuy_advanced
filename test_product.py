import pytest
import products


def test_product_creation():
    """Tests Product instance creation"""
    assert products.Product("test", price=1450, quantity=1000)


def test_create_product_without_name():
    """Tests Product instance creation with an empty string as name"""
    with pytest.raises(NameError, match="Name cannot be empty"):
        products.Product("", price=1450, quantity=1000)


def test_create_product_with_negative_price():
    """Tests Product instance creation with a negative price"""
    with pytest.raises(ValueError, match="Price/Quantity cannot be negative") :
        products.Product("test", price=-1450, quantity=1000)


def test_create_product_with_no_quantity():
    """Tests Product instance creation with zero quantity"""
    test = products.Product("test", price=1450, quantity=0)
    assert test.is_active() == False

def test_product_becomes_inactive():
    """Tests active status of the Product instance after buying the entire stock"""
    test = products.Product("test", price=1450, quantity=100)
    test.buy(100)
    assert test.is_active() == False


def test_product_purchase_quantity_update():
    """Tests Product instance quantity update after purchasing some of the products"""
    test = products.Product("test", price=1450, quantity=100)
    test.buy(50)
    assert test.quantity == 50

def test_buy_larger_quantity_than_available():
    """Tests Product instance handling if a greater amount than available is purchased"""
    test = products.Product("test", price=1450, quantity=100)
    with pytest.raises(ValueError, match="Quantity cannot be negative"):
        test.buy(101)
