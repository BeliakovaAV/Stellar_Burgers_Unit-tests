import pytest
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from unittest.mock import patch
from praktikum_stellar.database import Database


class TestDatabase:
    @pytest.mark.parametrize("expected_names, expected_prices",
                             [(["black bun", "white bun", "red bun"], [100, 200, 300])])
    def test_available_buns_returns_buns_correctly(self, database, expected_names, expected_prices):
        buns = database.available_buns()
        assert len(buns) == 3

        actual_names = []
        for b in buns:
            actual_names.append(b.name)

        actual_prices = []
        for b in buns:
            actual_prices.append(b.price)
        assert actual_names == expected_names
        assert actual_prices == expected_prices

    @pytest.mark.parametrize("ingredient_type, expected_names, expected_prices",
                             [(INGREDIENT_TYPE_SAUCE, ["hot sauce", "sour cream", "chili sauce"], [100, 200, 300]),
                              (INGREDIENT_TYPE_FILLING, ["cutlet", "dinosaur", "sausage"], [100, 200, 300])])
    def test_available_ingredients_by_type(self, database, ingredient_type, expected_names, expected_prices):
        ingredients_list = database.available_ingredients()
        new_list = []
        for ing in ingredients_list:
            if ing.type == ingredient_type:
                new_list.append(ing)
        assert len(new_list) == 3

        actual_names = []
        for ing in new_list:
            actual_names.append(ing.name)

        actual_prices = []
        for ing in new_list:
            actual_prices.append(ing.price)

        actual_type = []
        for ing in new_list:
            actual_type.append(ing.type)

        assert actual_names == expected_names
        assert actual_prices == expected_prices
        assert actual_type == [ingredient_type] * 3

    def test_calls_bun_and_ingredient(self, fake_bun, fake_ingredient):
        bun_mock, bun_calls = fake_bun
        ingredient_mock, ingredient_calls = fake_ingredient

        with patch('praktikum_stellar.database.Bun', new=bun_mock), \
                patch('praktikum_stellar.database.Ingredient', new=ingredient_mock):
            database = Database()

            assert bun_calls == [
                ("black bun", 100),
                ("white bun", 200),
                ("red bun", 300),
            ]

        assert ingredient_calls == [
            (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
            (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
            (INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
            (INGREDIENT_TYPE_FILLING, "cutlet", 100),
            (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
            (INGREDIENT_TYPE_FILLING, "sausage", 300),
        ]
        assert database.buns == ["Булка"] * 3
        assert database.ingredients == ["Ингредиент"] * 6
