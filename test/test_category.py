def test_category(first_category, second_category):
    assert first_category.name == "Category"
    assert first_category.description == "Description of the category"
    assert (
        first_category.get_product_list
        == "Product, 84.5 руб. Остаток: 10 шт.\nProduct number two, 155.87 руб. Остаток: 34 шт.\n"
    )

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 5
    assert second_category.product_count == 5
