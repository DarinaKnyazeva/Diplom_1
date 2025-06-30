import random

import pytest

import bun
import database
from bun import Bun
from burger import Burger


class TestBurger:

    def test_bun_of_burger_none(self):
        burger = Burger()
        assert burger.bun is None

    def test_ingredient_of_burger_is_empty_list(self):
        burger = Burger()
        assert burger.ingredients == []

    @pytest.mark.parametrize('bun_name', database.Database().available_buns())
    def test_ingredient_set_bun_true(self, bun_name):
        burger = Burger()
        burger.set_buns(bun_name)
        assert burger.bun == bun_name

    @pytest.mark.parametrize('ingredient', database.Database().available_ingredients())
    def test_add_ingredient_true(self, ingredient):
        burger = Burger()
        burger.add_ingredient(ingredient)
        assert burger.ingredients == [ingredient]

    @pytest.mark.parametrize('ingredient', database.Database().available_ingredients())
    def test_remove_ingredient_true(self, ingredient):
        burger = Burger()
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient_true(self):
        burger = Burger()
        ingredient_list = database.Database().available_ingredients()
        burger.ingredients = database.Database().available_ingredients()
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0].name == ingredient_list[1].name

    def test_burger_get_price_true(self):
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

    def test_burger_get_receipt_true(self):
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
