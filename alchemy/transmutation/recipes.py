def lead_to_gold() -> str:
    from ..potions import strength_potion
    from ..elements import create_air
    from elements import create_fire

    air: str = create_air()
    strength: str = strength_potion()
    fire: str = create_fire()

    return f"'{air}' and '{strength}' mixed with '{fire}'"
