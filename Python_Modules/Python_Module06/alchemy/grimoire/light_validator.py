def validate_ingredients(ingredients: str) -> str:
    allowed = ["earth", "air", "fire", "water"]
    for ingredient in allowed:
        if ingredient in ingredients.lower():
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
