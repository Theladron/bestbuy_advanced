import pytest
import products

def test_product_creation():
    assert products.Product("test", price=1450, quantity=1000)


def test_create_product_without_name():
    with pytest.raises(NameError, match="Name cannot be empty"):
        products.Product("", price=1450, quantity=1000)


def test_create_product_with_negative_price():
    with pytest.raises(ValueError, match="Price/Quantity cannot be negative") :
        products.Product("test", price=-1450, quantity=1000)


def test_create_product_with_no_quantity():
    test = products.Product("test", price=1450, quantity=0)
    assert test.is_active() == False

def test_product_becomes_inavtive():
    test = products.Product("test", price=1450, quantity=100)
    test.buy(100)
    assert test.is_active() == False


def test_product_purchase_quantity_update():
    test = products.Product("test", price=1450, quantity=100)
    test.buy(50)
    assert test.get_quantity() == 50

def test_buy_larger_quantity_than_available():
    test = products.Product("test", price=1450, quantity=100)
    with pytest.raises(ValueError, match="Quantity larger then what exists"):
        test.buy(101)
