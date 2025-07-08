import pytest

from praktikum import database
from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize('available_bun', database.Database().available_buns())
    def test_name_of_bun(self, available_bun):
        bun = Bun(available_bun.name, available_bun.price)
        assert bun.name == available_bun.name

    @pytest.mark.parametrize('available_bun', database.Database().available_buns())
    def test_price_of_bun(self, available_bun):
        bun = Bun(available_bun.name, available_bun.price)
        assert bun.price == available_bun.price

    @pytest.mark.parametrize('available_bun', database.Database().available_buns())
    def test_get_name_of_bun(self, available_bun):
        bun = Bun(available_bun.name, available_bun.price)
        bun_list = bun.get_name()
        assert bun_list == available_bun.name

    @pytest.mark.parametrize('available_bun', database.Database().available_buns())
    def test_get_price_of_bun(self, available_bun):
        bun = Bun(available_bun.name, available_bun.price)
        bun_price = bun.get_price()
        assert bun_price == available_bun.price