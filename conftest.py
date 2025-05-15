import pytest
import data
from bun import Bun
from ingredient import Ingredient
from burger import Burger
import ingredient_types


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


