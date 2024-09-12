#  класс содержит юнит-тесты для проверки работы методов класса Database
from data_for_tests.data import Data
from praktikum.bun import Bun
from praktikum.database import Database


class TestDatabase:

    #  позитивная проверка работы метода 'available_buns'
    def test_available_buns(self):
        db = Database()
        buns = db.available_buns()
        assert buns[1].name == Data.BUN_NAME_2 and buns[2].name == Data.BUN_NAME_1

    # позитивная проверка работы метода 'available_ingredients'
    def test_available_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert ingredients[0].name == Data.SAUCE_NAME_1 and ingredients[4].name == Data.FILLING_NAME_1
