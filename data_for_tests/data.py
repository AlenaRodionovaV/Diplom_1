#  класс содержит вспомогательные тестовые данные для подстановки в юнит-тесты
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class Data:
    #  название булочек
    BUN_NAME_1 = 'red bun'
    BUN_NAME_2 = 'white bun'

    #  стоимость булочек
    BUN_PRICE_1 = 100
    BUN_PRICE_2 = 200

    #  название соусов
    SAUCE_NAME_1 = 'hot sauce'
    SAUCE_NAME_2 = 'sour cream'

    #  стоимость соусов
    SAUCE_PRICE_1 = 200
    SAUCE_PRICE_2 = 300

    #  название начинок
    FILLING_NAME_1 = 'dinosaur'
    FILLING_NAME_2 = 'sausage'

    #  стоимость начинок
    FILLING_PRICE_1 = 300
    FILLING_PRICE_2 = 300

    #  типы начинок
    TYPE_SAUCE = INGREDIENT_TYPE_SAUCE
    TYPE_FILLING = INGREDIENT_TYPE_FILLING
