import pytest

import database
from ingredient import Ingredient


class TestIngredient:

    @pytest.mark.parametrize('ingredient_type', database.Database().available_ingredients())
    def test_name_of_ingredient_true(self, ingredient_type):
        ingredient = Ingredient(ingredient_type.type, ingredient_type.name, ingredient_type.price)
        assert ingredient.type == ingredient_type.type

    @pytest.mark.parametrize('ingredient_name', database.Database().available_ingredients())
    def test_name_of_ingredient_true(self, ingredient_name):
        ingredient = Ingredient(ingredient_name.type, ingredient_name.name, ingredient_name.price)
        assert ingredient.name == ingredient_name.name

    @pytest.mark.parametrize('ingredient_price', database.Database().available_ingredients())
    def test_name_of_ingredient_true(self, ingredient_price):
        ingredient = Ingredient(ingredient_price.type, ingredient_price.name, ingredient_price.price)
        assert ingredient.price == ingredient_price.price

    @pytest.mark.parametrize('ingredient_price', database.Database().available_ingredients())
    def test_get_price_of_ingredient_true(self, ingredient_price):
        ingredient = Ingredient(ingredient_price.type, ingredient_price.name, ingredient_price.price)
        ingredients_price = ingredient.get_price()
        assert ingredient.price == ingredients_price

    @pytest.mark.parametrize('ingredient_name', database.Database().available_ingredients())
    def test_get_name_of_ingredient_true(self, ingredient_name):
        ingredient = Ingredient(ingredient_name.type, ingredient_name.name, ingredient_name.price)
        ingredients_name = ingredient.get_name()
        assert ingredient.name == ingredients_name

    @pytest.mark.parametrize('ingredient_type', database.Database().available_ingredients())
    def test_get_type_of_ingredient_true(self, ingredient_type):
        ingredient = Ingredient(ingredient_type.type, ingredient_type.name, ingredient_type.price)
        ingredients_type = ingredient.get_type()
        assert ingredient.type == ingredients_type