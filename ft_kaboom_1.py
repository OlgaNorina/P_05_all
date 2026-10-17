def main() -> None:
    print(
        "=== Kaboom 1 ===\n"
        "Access to alchemy/grimoire/dark_spellbook.py directly"
    )

    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION: ")

    from alchemy.grimoire.dark_spellbook import dark_spell_record
    
    print(f"{light_spell_record("Lumos", "fire, Stardust")}")


if __name__ == "__main__":
    main()