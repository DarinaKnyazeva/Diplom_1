import pytest

import database
from bun import Bun


class TestBun:

    @pytest.mark.parametrize('bun_name', database.Database().available_buns())
    def test_name_of_bun_true(self, bun_name):
        bun = Bun(bun_name.name, bun_name.price)
        assert bun.name == bun_name.name

    @pytest.mark.parametrize('bun_price', database.Database().available_buns())
    def test_price_of_bun_true(self, bun_price):
        bun = Bun(bun_price.name, bun_price.price)
        assert bun.price == bun_price.price

    @pytest.mark.parametrize('bun_name', database.Database().available_buns())
    def test_get_name_of_bun_true(self, bun_name):
        bun = Bun(bun_name.name, bun_name.price)
        bun_list = bun.get_name()
        assert bun_list == bun_name.name

    @pytest.mark.parametrize('bun_price', database.Database().available_buns())
    def test_get_price_of_bun_true(self, bun_price):
        bun = Bun(bun_price.name, bun_price.price)
        bun_list = bun.get_price()
        assert bun_list == bun_price.price