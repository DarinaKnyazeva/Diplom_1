import pytest

from praktikum import database
from praktikum.ingredient import Ingredient


class TestIngredient:

    @pytest.mark.parametrize('available_ingredient', database.Database().available_ingredients())
    def test_name_of_ingredient(self, available_ingredient):
        ingredient = Ingredient(available_ingredient.type, available_ingredient.name, available_ingredient.price)
        assert ingredient.type == available_ingredient.type

    @pytest.mark.parametrize('available_ingredient', database.Database().available_ingredients())
    def test_name_of_ingredient(self, available_ingredient):
        ingredient = Ingredient(available_ingredient.type, available_ingredient.name, available_ingredient.price)
        assert ingredient.name == available_ingredient.name

    @pytest.mark.parametrize('available_ingredient', database.Database().available_ingredients())
    def test_name_of_ingredient(self, available_ingredient):
        ingredient = Ingredient(available_ingredient.type, available_ingredient.name, available_ingredient.price)
        assert ingredient.price == available_ingredient.price

    @pytest.mark.parametrize('available_ingredient', database.Database().available_ingredients())
    def test_get_price_of_ingredient(self, available_ingredient):
        ingredient = Ingredient(available_ingredient.type, available_ingredient.name, available_ingredient.price)
        ingredients_price = ingredient.get_price()
        assert ingredients_price == available_ingredient.price

    @pytest.mark.parametrize('available_ingredient', database.Database().available_ingredients())
    def test_get_name_of_ingredient(self, available_ingredient):
        ingredient = Ingredient(available_ingredient.type, available_ingredient.name, available_ingredient.price)
        ingredients_name = ingredient.get_name()
        assert ingredients_name == available_ingredient.name

    @pytest.mark.parametrize('available_ingredient', database.Database().available_ingredients())
    def test_get_type_of_ingredient(self, available_ingredient):
        ingredient = Ingredient(available_ingredient.type, available_ingredient.name, available_ingredient.price)
        ingredients_type = ingredient.get_type()
        assert ingredients_type == available_ingredient.type
