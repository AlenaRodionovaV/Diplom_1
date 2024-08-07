from praktikum.burger import Burger


class TestBurger:
    def test_set_buns_positive(self):
        burger = Burger()
        bun = MockBun("Краторная булка", 1255)
        burger.set_buns(bun)
        assert burger.bun == bun