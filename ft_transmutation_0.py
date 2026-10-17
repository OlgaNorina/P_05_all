import alchemy.transmutation.recipes


def main() -> None:
    print("=== Transmutation 0 ===")
    print("Using file alchemy/transmutation/recipes.py directly")

    try:
        print("Testing lead to gold: ", end="")
        print("Recipe transmuting Lead to Gold: brew ", end="")
        print(f"{alchemy.transmutation.recipes.lead_to_gold()}")
    except Exception as err:
        print(f"{err}")


if __name__ == "__main__":
    main()
