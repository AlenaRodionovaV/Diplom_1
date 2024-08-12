from data_for_tests.data import Data
from data_for_tests.mock_data import make_mock_bun, make_mock_sauce_1, make_mock_filling_2, make_mock_filling_1, \
    make_mock_sauce_2, make_mock_burger
from praktikum.burger import Burger
from unittest.mock import call


#  класс содержит юнит-тесты для проверки работы методов класса Burger
class TestBurger:

    #  позитивная проверка работы метода 'set_buns'
    def test_set_buns(self):
        burger = Burger()
        mock_bun = make_mock_bun()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun and burger.bun.name == mock_bun.name and burger.bun.price == mock_bun.price

    #  позитивная проверка работы метода 'add_ingredient'
    def test_add_ingredient(self):
        burger = Burger()
        mock_bun = make_mock_bun()
        mock_sauce = make_mock_sauce_1()
        mock_filling = make_mock_filling_1()
        #  добавляем ингредиенты  в бургер
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        #  проверяем, что ингредиенты добавились, и что ингредиенты установились в правильном порядке
        assert burger.ingredients[0] == mock_sauce and burger.ingredients[1] == mock_filling

    #  позитивная проверка работы метода 'remove_ingredient'
    def test_remove_ingredient(self):
        burger = Burger()
        mock_bun = make_mock_bun()
        mock_sauce = make_mock_sauce_1()
        mock_filling = make_mock_filling_1()
        #  добавляем ингредиенты  в бургер
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        #  удаляем первый ингредиент
        burger.remove_ingredient(0)
        #  проверяем, что остался только один ингредиент - начинка
        assert len(burger.ingredients) == 1 and burger.ingredients[0] == mock_filling

    #  позитивная проверка работы метода 'move_ingredient'
    def test_move_ingredient(self):
        burger = Burger()
        mock_bun = make_mock_bun()
        #  создаем пару экземпляров соусов и начинок
        mock_sauce_1 = make_mock_sauce_1()
        mock_sauce_2 = make_mock_sauce_2()
        mock_filling_1 = make_mock_filling_1()
        #  добавляем ингредиенты  в бургер
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce_1)
        burger.add_ingredient(mock_sauce_2)
        burger.add_ingredient(mock_filling_1)
        #  перемещаем начинку 1 на первое место перед соусом 1
        burger.move_ingredient(2, 0)
        assert (burger.ingredients[0] == mock_filling_1 and burger.ingredients[1] == mock_sauce_1 and
                burger.ingredients[2] == mock_sauce_2)

    #  позитивная проверка работы метода 'get_price'
    def test_get_price(self):
        burger = Burger()
        mock_bun = make_mock_bun()
        mock_sauce = make_mock_sauce_1()
        mock_filling = make_mock_filling_1()
        #  добавляем ингредиенты  в бургер
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        #  устанавливаем стоимость ингредиентов
        mock_bun.get_price.return_value = 200
        mock_sauce.get_price.return_value = 100
        mock_filling.get_price.return_value = 300
        #  считаем ожидаемую стоимость
        expected_price = (mock_bun.get_price() * 2) + mock_sauce.get_price() + mock_filling.get_price()
        assert burger.get_price() == expected_price
        #  проверяем, что метод 'get_price' был вызван на булочке и ингредиентах
        mock_bun.get_price.assert_has_calls([call()])
        mock_sauce.get_price.assert_has_calls([call()])
        mock_filling.get_price.assert_has_calls([call()])

    #  позитивная проверка работы метода 'get_receipt'
    def test_get_receipt(self):
        burger = Burger()
        mock_bun = make_mock_bun()
        mock_sauce = make_mock_sauce_1()
        mock_filling = make_mock_filling_1()
        #  добавляем ингредиенты  в бургер
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        #  формируем название ингредиентов и их стоимость
        mock_bun.get_name.return_value = Data.BUN_NAME_1
        mock_bun.get_price.return_value = Data.BUN_PRICE_1
        mock_sauce.get_name.return_value = Data.SAUCE_NAME_1
        mock_sauce.get_price.return_value = Data.SAUCE_PRICE_1
        mock_sauce.get_type.return_value = Data.TYPE_SAUCE
        mock_filling.get_name.return_value = Data.FILLING_NAME_1
        mock_filling.get_price.return_value = Data.FILLING_PRICE_1
        mock_filling.get_type.return_value = Data.TYPE_FILLING
        #  формируем ожидаемый чек
        expected_receipt = (
            f"(==== red bun ====)\n"
            f"= sauce hot sauce =\n"
            f"= filling dinosaur =\n"
            f"(==== red bun ====)\n"
            f"Price: 700"
        )
        assert expected_receipt == burger.get_receipt()
