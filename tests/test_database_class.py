from praktikum.database import Database


class TestDataBase:

    def test_available_buns_is(self):
        database = Database()
        expected_buns = database.buns
        actual_buns = database.available_buns()

        for expected_bun, actual_bun in zip(expected_buns, actual_buns):
            assert expected_bun.name == actual_bun.name

        assert len(actual_buns) == len(expected_buns)

    def test_available_ingredients(self):
        database = Database()
        expected_ingredients = database.ingredients
        actual_ingredients = database.available_ingredients()

        for expected_ingredient, actual_ingredient in zip(expected_ingredients, actual_ingredients):
            assert expected_ingredient.name == actual_ingredient.name

        assert len(actual_ingredients) == len(expected_ingredients)
