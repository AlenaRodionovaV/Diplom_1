#  модуль содержит методы, которые создают мок-объекты

from unittest.mock import Mock
from data_for_tests.data import Data
from praktikum.burger import Burger


#  метод для создания мок-объекта булочки
def make_mock_bun():
    mock_bun = Mock()
    mock_bun.name = Data.BUN_NAME_1
    mock_bun.price = Data.BUN_PRICE_1
    return mock_bun


#  метод для создания мок-объекта соуса, 1 вариант
def make_mock_sauce_1():
    mock_sauce = Mock()
    mock_sauce.name = Data.SAUCE_NAME_1
    mock_sauce.price = Data.SAUCE_PRICE_1
    mock_sauce.type = Data.TYPE_SAUCE
    return mock_sauce


#  метод для создания мок-объекта соуса, 2 вариант
def make_mock_sauce_2():
    mock_sauce = Mock()
    mock_sauce.name = Data.SAUCE_NAME_2
    mock_sauce.price = Data.SAUCE_PRICE_2
    mock_sauce.type = Data.TYPE_SAUCE
    return mock_sauce


#  метод для создания мок-объекта начинки, 1 вариант
def make_mock_filling_1():
    mock_filling = Mock()
    mock_filling.name = Data.FILLING_NAME_1
    mock_filling.price = Data.FILLING_PRICE_1
    mock_filling.type = Data.TYPE_FILLING
    return mock_filling


#  метод для создания мок-объекта начинки, 2 вариант
def make_mock_filling_2():
    mock_filling = Mock()
    mock_filling.name = Data.FILLING_NAME_2
    mock_filling.price = Data.FILLING_PRICE_2
    mock_filling.type = Data.TYPE_FILLING
    return mock_filling


#  метод для создания мок-объекта бургер
def make_mock_burger():
    burger = Burger()
    mock_bun = make_mock_bun()
    mock_sauce = make_mock_sauce_1()
    mock_filling = make_mock_filling_1()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_sauce)
    burger.add_ingredient(mock_filling)
    return burger, mock_bun, mock_sauce, mock_filling

