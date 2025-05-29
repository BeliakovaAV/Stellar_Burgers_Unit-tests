import data
import pytest
import ingredient_types

from Diplom_1.praktikum_stellar.bun import Bun
from Diplom_1.praktikum_stellar.burger import Burger
from Diplom_1.praktikum_stellar.database import Database
from Diplom_1.praktikum_stellar.ingredient import Ingredient


@pytest.fixture
def wholegrain_bun():
    return Bun(data.BUN_NAME, data.BUN_PRICE)


@pytest.fixture
def cheese_sauce():
    return Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE, data.SAUCE_NAME, data.SAUCE_PRICE)


@pytest.fixture
def meat_filling():
    return Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, data.FILLING_NAME, data.FILLING_PRICE)


@pytest.fixture
def empty_burger():
    return Burger()


@pytest.fixture
def bun_burger(empty_burger, wholegrain_bun):
    empty_burger.set_buns(wholegrain_bun)
    return empty_burger


@pytest.fixture
def database():
    return Database()


@pytest.fixture
def fake_bun():
    calls = []

    def _fake_bun(name, price):
        calls.append((name, price))
        return "Булка"

    return _fake_bun, calls


@pytest.fixture
def fake_ingredient():
    calls = []

    def _fake_ingredient(type_, name, price):
        calls.append((type_, name, price))
        return "Ингредиент"

    return _fake_ingredient, calls
