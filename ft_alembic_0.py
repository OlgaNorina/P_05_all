def main() -> None:
    print(
            "=== Alembic 0 ==="
            "\nUsing: 'import ...' structure to access elements.py"
    )

    from elements import create_fire

    print("Testing create_fire:", end=" ")
    try:
        print(f"{create_fire()}\n")
    except AttributeError as err:
        print(f"{err}")


if __name__ == "__main__":
    main()
