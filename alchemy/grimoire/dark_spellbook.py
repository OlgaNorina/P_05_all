from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    ingredients: list[str] = ["bats", "frogs", "arsenic", "eye￾ball"]
    return ingredients


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    validate: str = validate_ingredients(ingredients)

    if "VALID" in validate and "INVALID" not in validate:
        return f"Spell recorded: {spell_name} ({ingredients} - VALID)"
    return f"Spell rejected: {spell_name} ({ingredients} - INVALID)"