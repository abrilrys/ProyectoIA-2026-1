import json

RECIPIES_FILE = "all_mexican_recipes.json"


def load_mock_recipe():
    data = load_json(RECIPIES_FILE)
    recipe = data[0]
    return data, recipe


def load_json(file_name: str) -> dict:
    with open(file_name, "r") as f:
        data = json.load(f)
    return data


def extract_ingredients(data: list[dict]) -> set[str]:
    result = set()
    for recipe in data:
        for ingredient in recipe["extendedIngredients"]:
            result.add(ingredient["name"])
    return result


def get_nutrient(recipe, name):
    """Helper to extract specific nutrient from the complex JSON list."""
    for nut in recipe["nutrition"]["nutrients"]:
        if nut["name"] == name:
            return f"{nut['amount']:.0f}{nut['unit']}"
    return "0"


def generate_weekly_plan(mock_recipe: dict):
    """Simulates your friend's logic: Generates 3 meals for 7 days."""
    days = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    plan = {}

    # We create 3 copies of the mock recipe per day for demonstration

    for day in days:
        plan[day] = [
            {
                **mock_recipe,
                "title": f"Desayuno: {mock_recipe['title']}",
                "meal_type": "Desayuno",
            },
            {
                **mock_recipe,
                "title": f"Comida: {mock_recipe['title']}",
                "meal_type": "Comida",
            },
            {
                **mock_recipe,
                "title": f"Cena: {mock_recipe['title']}",
                "meal_type": "Cena",
            },
        ]
    return plan
