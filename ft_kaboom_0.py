def main() -> None:
    print(
        "=== Kaboom 0 ===\n"
        "Using grimoire module directly"
    )
    from alchemy.grimoire.light_spellbook import light_spell_record

    print(f"Testing record light spell: {light_spell_record("Lumos", "fire, Stardust")}")


if __name__ == "__main__":
    main()
