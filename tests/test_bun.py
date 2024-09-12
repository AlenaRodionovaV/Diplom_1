import pytest
from data_for_tests.data import Data
from praktikum.bun import Bun


#  класс содержит юнит-тесты для проверки работы методов класса Bun
class TestBun:

    #  позитивная проверка работы метода 'get_name'
    @pytest.mark.parametrize(
        'name,price',
        [
            [Data.BUN_NAME_1, Data.BUN_PRICE_1],
            [Data.BUN_NAME_2, Data.BUN_PRICE_2]
        ]
    )
    def test_get_name_positive(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    #  позитивная проверка работы метода 'get_price'
    @pytest.mark.parametrize(
        'name,price',
        [
            [Data.BUN_NAME_1, Data.BUN_PRICE_1],
            [Data.BUN_NAME_2, Data.BUN_PRICE_2]
        ]
    )
    def test_get_price_positive(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price

    #  негативная проверка метода 'get_name' при возвращении пустого 'name'
    def test_get_name_if_name_is_empty_negative(self):
        bun = Bun("", Data.BUN_PRICE_1)
        assert bun.get_name() == ""

    #  негативная проверка метода 'get_price', если в 'price' передано не число, а строка
    def test_get_price_if_string_negative(self):
        bun = Bun(Data.BUN_NAME_1, "Тысяча")
        price = bun.get_price()
        assert not isinstance(price, float)
