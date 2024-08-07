#  модуль содержит методы, которые создают мок-объекты

import pytest
from unittest.mock import Mock
from data_for_tests.data import Data
from praktikum.burger import Burger


#  метод для создания мок-объекта булочки
def make_mock_bun():
    mock_bun = Mock()
    mock_bun.name = Data.BUN_NAME_1
    mock_bun.price = Data.BUN_PRICE_1
    return mock_bun


#  метод для создания мок-объекта соуса
def make_mock_sauce():
    mock_sauce = Mock()
    mock_sauce.name = Data.SAUCE_NAME_1
    mock_sauce.price = Data.SAUCE_PRICE_1
    return mock_sauce


#  метод для создания мок-объекта начинки
def make_mock_filling():
    mock_filling = Mock()
    mock_filling.name = Data.FILLING_NAME_1
    mock_filling.price = Data.FILLING_PRICE_1
    return mock_filling


#  метод для создания мок-объекта бургер
def make_mock_burger():
    mock_burger = Mock()
    mock_burger.name = Data.FILLING_NAME_1
    mock_burger.price = Data.FILLING_PRICE_1
    return mock_burger
