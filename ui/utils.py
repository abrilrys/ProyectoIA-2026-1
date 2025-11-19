import json


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
