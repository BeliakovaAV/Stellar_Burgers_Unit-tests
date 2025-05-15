import pytest
from bun import Bun
import data


class TestBun:
    def test_setting_bun_name_and_price(self, wholegrain_bun):
        assert wholegrain_bun.name == data.BUN_NAME
        assert wholegrain_bun.price == data.BUN_PRICE

    def test_get_name_returns_correct_name(self, wholegrain_bun):
        assert wholegrain_bun.get_name() == data.BUN_NAME

    def test_get_price_returns_correct_price(self, wholegrain_bun):
        assert wholegrain_bun.get_price() == data.BUN_PRICE

    @pytest.mark.parametrize("name, price", [(12345, "18 рублей"), ("Маковая", None)])
    def test_invalid_name_price_types(self, name, price):
        with pytest.raises(TypeError):
            Bun(name, price)
