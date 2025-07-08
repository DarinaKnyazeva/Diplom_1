import random
from unittest.mock import Mock

import pytest

from praktikum import database
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient


class TestBurger:

    def test_bun_of_burger_none(self):
        burger = Burger()
        assert burger.bun is None

    def test_ingredient_of_burger_is_empty_list(self):
        burger = Burger()
        assert burger.ingredients == []

    @pytest.mark.parametrize('available_bun', database.Database().available_buns())
    def test_ingredient_set_bun(self, available_bun):
        burger = Burger()
        burger.set_buns(available_bun)
        assert burger.bun == available_bun

    @pytest.mark.parametrize('ingredient', database.Database().available_ingredients())
    def test_add_ingredient(self, ingredient):
        burger = Burger()
        burger.add_ingredient(ingredient)
        assert burger.ingredients == [ingredient]

    @pytest.mark.parametrize('ingredient', database.Database().available_ingredients())
    def test_remove_ingredient(self, ingredient):
        burger = Burger()
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient(self):
        burger = Burger()
        ingredient_list = database.Database().available_ingredients()
        burger.ingredients = database.Database().available_ingredients()
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0].name == ingredient_list[1].name

    def test_burger_get_price(self):
        burger = Burger()
        bun_list = database.Database().available_buns()
        random_bun = random.choice(bun_list)
        ingredient_list = database.Database().available_ingredients()
        random_ingredient = random.choice(ingredient_list)
        burger.set_buns(random_bun)
        burger.add_ingredient(random_ingredient)
        actual_price = burger.get_price()
        expected_price = random_bun.price * 2 + random_ingredient.price
        assert actual_price == expected_price

    def test_get_price_burger_with_mock(self):
        bun_mock = Mock()
        ingredient_mock = Mock()
        bun_mock.get_price.return_value = 100
        ingredient_mock.get_price.return_value = 100
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
        assert burger.get_price() == 300

    def test_burger_get_receipt(self):
        burger = Burger()
        bun_list = database.Database().available_buns()
        random_bun = random.choice(bun_list)
        ingredient_list = database.Database().available_ingredients()
        random_ingredient = random.choice(ingredient_list)
        burger.set_buns(random_bun)
        burger.add_ingredient(random_ingredient)
        actual_receipt = burger.get_receipt()
        expected_receipt = f'(==== {random_bun.get_name()} ====)\n= {str(random_ingredient.get_type()).lower()} {random_ingredient.get_name()} =\n(==== {random_bun.get_name()} ====)\n\nPrice: {burger.get_price()}'
        assert actual_receipt == expected_receipt
