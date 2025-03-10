import pytest
from src.product import Product


def test_product(first_product, second_product):
    assert first_product.name == "Product"
    assert first_product.description == "Description of the product"
    assert first_product.price == 84.50
    assert first_product.quantity == 10

    assert second_product.name == "Product number two"
    assert second_product.description == "Description of the product number two"
    assert second_product.price == 155.87
    assert second_product.quantity == 34


def test_new_product(product_dict):
    product4 = Product.new_product(product_dict)
    assert product4.name == "Product 4"
    assert product4.description == "Description of the product 4"
    assert product4.price == 145.75
    assert product4.quantity == 23


def test_product_str(first_product):
    assert str(first_product) == "Product, 84.5 руб. Остаток: 10 шт."


def test_product_add(first_product, second_product):
    assert first_product + second_product == 6144.58


def test_smartphone_init(smartphone1):
    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone1.price == 180000.0
    assert smartphone1.quantity == 5
    assert smartphone1.efficiency == 95.5
    assert smartphone1.model == "S23 Ultra"
    assert smartphone1.memory == 256
    assert smartphone1.color == "Серый"


def test_add_smartphone(smartphone1, smartphone2):
    assert smartphone1 + smartphone2 == 2580000.0


def test_add_smartphone_error(smartphone1):
    with pytest.raises(TypeError):
        smartphone1 + 1


def test_lawn_grass_init(lawn_grass1):
    assert lawn_grass1.name == "Газонная трава"
    assert lawn_grass1.description == "Элитная трава для газона"
    assert lawn_grass1.price == 500.0
    assert lawn_grass1.quantity == 20
    assert lawn_grass1.country == "Россия"
    assert lawn_grass1.germination_period == "7 дней"
    assert lawn_grass1.color == "Зеленый"


def test_add_grass(lawn_grass1, lawn_grass2):
    grass_sum = lawn_grass1 + lawn_grass2
    assert grass_sum == 16750.0


def test_add_grass_error(lawn_grass1):
    with pytest.raises(TypeError):
        lawn_grass1 + 1


def test_print_mixin(capsys) -> None:
    Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    massage = capsys.readouterr()
    assert (massage.out.strip() == 'Product(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)')


def test_product_add_error(smartphone2, lawn_grass2):
    with pytest.raises(TypeError):
        smartphone2 + lawn_grass2
        smartphone2 + 3


def test_empty_product() -> None:
    with pytest.raises(ValueError) as e:
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    assert str(e.value) == "Товар с нулевым количеством не может быть добавлен"
