def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients

    allowed: list[str] = light_spell_allowed_ingredients()
    is_valid: bool = False

    for item in ingredients.split(','):
        if item.strip().lower() in allowed:
            is_valid = True
            break
    status: str = "VALID" if is_valid else "INVALID"
    return f"{ingredients}, {status}"
        