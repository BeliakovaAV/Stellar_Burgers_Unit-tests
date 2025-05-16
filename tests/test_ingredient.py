import data
import ingredient_types
from praktikum_stellar.ingredient import Ingredient


class TestIngredient:
    def test_setting_ingredient(self, cheese_sauce):
        assert cheese_sauce.name == data.SAUCE_NAME
        assert cheese_sauce.price == data.SAUCE_PRICE
        assert cheese_sauce.type == ingredient_types.INGREDIENT_TYPE_SAUCE

    def test_get_name_returns_correct_name(self, cheese_sauce):
        assert cheese_sauce.get_name() == data.SAUCE_NAME

    def test_get_price_returns_correct_price(self, meat_filling):
        assert meat_filling.get_price() == data.FILLING_PRICE

    def test_get_type_returns_correct_type(self, meat_filling):
        assert meat_filling.get_type() == ingredient_types.INGREDIENT_TYPE_FILLING
