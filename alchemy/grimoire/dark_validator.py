from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed: list[str] = dark_spell_allowed_ingredients(ingredients)
    is_valid: bool = False

    for item in ingredients.split(','):
        if item.strip().lower() in allowed:
            is_valid = True
            break
    
    status: str = "VALID" if is_valid else "INVALID"
    return f"{ingredients}, {status}"
