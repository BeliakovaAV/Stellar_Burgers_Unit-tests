import pytest
from bun import Bun
from ingredient import Ingredient
import data
import ingredient_types


class TestBurger:
    def test_set_buns(self, empty_burger, wholegrain_bun):
        empty_burger.set_buns(wholegrain_bun)
        assert empty_burger.bun == wholegrain_bun

    def test_add_one_ingredient(self, bun_burger, meat_filling):
        bun_burger.add_ingredient(meat_filling)
        assert bun_burger.ingredients == [meat_filling]

    def test_remove_one_ingredient(self, bun_burger, cheese_sauce):
        bun_burger.add_ingredient(cheese_sauce)
        bun_burger.remove_ingredient(0)
        assert bun_burger.ingredients == []

    def test_remove_no_ingredient(self, bun_burger):
        with pytest.raises(IndexError):
            bun_burger.remove_ingredient(0)

    def test_move_ingredient(self, bun_burger, meat_filling, cheese_sauce):
        bun_burger.add_ingredient(meat_filling)
        bun_burger.add_ingredient(cheese_sauce)
        bun_burger.move_ingredient(0, 1)
        assert bun_burger.ingredients == [cheese_sauce, meat_filling]

    @pytest.mark.parametrize("bun_price, ingredient_price, expected_total", [
        (1.05, [], 2.1),
        (7.0, [0.8], 14.8),
        (5.3, [1.6, 4.4], 16.6),
    ])
    def test_get_different_price(self, empty_burger, bun_price, ingredient_price, expected_total):
        empty_burger.set_buns(Bun(data.BUN_NAME, bun_price))
        for price in ingredient_price:
            empty_burger.add_ingredient(Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, data.FILLING_NAME, price))
        assert empty_burger.get_price() == expected_total

    def test_get_receipt(self, bun_burger, meat_filling, cheese_sauce):
        bun_burger.add_ingredient(meat_filling)
        bun_burger.add_ingredient(cheese_sauce)
        receipt = bun_burger.get_receipt()
        total = (data.BUN_PRICE * 2 + data.FILLING_PRICE + data.SAUCE_PRICE)
        expected = "\n".join([
            f"(==== {data.BUN_NAME} ====)",
            f"= {ingredient_types.INGREDIENT_TYPE_FILLING.lower()} {data.FILLING_NAME} =",
            f"= {ingredient_types.INGREDIENT_TYPE_SAUCE.lower()} {data.SAUCE_NAME} =",
            f"(==== {data.BUN_NAME} ====)\n",
            f"Price: {total}"
        ])
        assert receipt == expected
