import pytest
from bun import Bun


class TestBun:
    def test_setting_bun_name_and_price(self, wholegrain_bun):
        assert wholegrain_bun.name == "Цельнозерновая"
        assert wholegrain_bun.price == 1.54

    def test_get_name_returns_correct_name(self, wholegrain_bun):
        assert wholegrain_bun.get_name() == "Цельнозерновая"

    def test_get_price_returns_correct_price(self, wholegrain_bun):
        assert wholegrain_bun.get_price() == 1.54

    @pytest.mark.parametrize("name, price", [(12345, "18 рублей"), ("Маковая", None)])
    def test_invalid_name_price_types(self, name, price):
        with pytest.raises(TypeError):
            Bun(name, price)
