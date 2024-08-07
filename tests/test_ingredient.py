import pytest
from data_for_tests.data import Data
from praktikum.ingredient import Ingredient


#  класс содержит юнит-тесты для проверки работы методов класса Ingredient
class TestIngredient:

    #  позитивная проверка работы метода 'get_name'
    @pytest.mark.parametrize(
        'ingredient_type,name,price',
        [
            [Data.TYPE_SAUCE, Data.SAUCE_NAME_1, Data.SAUCE_PRICE_1],
            [Data.TYPE_FILLING, Data.FILLING_NAME_1, Data.FILLING_PRICE_1]
        ]
    )
    def test_get_name_positive(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    #  негативная проверка работы метода 'get_name' при возвращении пустого 'name'
    def test_get_name_if_name_is_empty_negative(self):
        ingredient = Ingredient(Data.TYPE_SAUCE, "", Data.SAUCE_PRICE_1)
        assert ingredient.get_name() == ""

    #  позитивная проверка работы метода 'get_price'
    @pytest.mark.parametrize(
        'ingredient_type,name,price',
        [
            [Data.TYPE_SAUCE, Data.SAUCE_NAME_2, Data.SAUCE_PRICE_2],
            [Data.TYPE_FILLING, Data.FILLING_NAME_2, Data.FILLING_PRICE_2]
        ]
    )
    def test_get_price_positive(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price

    #  негативная проверка метода 'get_price', если в 'price' передано не число, а строка
    def test_get_price_if_string_negative(self):
        ingredient = Ingredient(Data.TYPE_SAUCE, Data.SAUCE_NAME_2, "Price")
        price = ingredient.get_price()
        assert not isinstance(price, float)

    #  позитивная проверка работы метода 'get_type'
    @pytest.mark.parametrize(
        'ingredient_type,name,price',
        [
            [Data.TYPE_SAUCE, Data.SAUCE_NAME_1, Data.SAUCE_PRICE_2],
            [Data.TYPE_FILLING, Data.FILLING_NAME_2, Data.FILLING_PRICE_1]
        ]
    )
    def test_get_type_positive(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
