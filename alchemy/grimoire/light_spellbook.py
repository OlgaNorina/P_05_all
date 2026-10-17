from .light_validator import validate_ingredients

def light_spell_allowed_ingredients() -> list[str]:
    ingredients: list[str] = ["earth", "air", "fire", "water"]
    return ingredients


def light_spell_record(spell_name: str, ingredients: str) -> str:
    validate: str = validate_ingredients(ingredients)
    if "VALID" in validate and "INVALID" not in validate:
        return f"Spell recorded: {spell_name} ({ingredients} - VALID)"
    return f"Spell rejected: {spell_name} ({ingredients} - INVALID)"
