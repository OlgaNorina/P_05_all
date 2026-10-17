from alchemy.potions import healing_potion, strength_potion

print("=== Distillation 0 ===")
print("Direct access to alchemy/potions.py")
try:
    print(f"Texting strength_potion: {strength_potion()}")
except Exception as err:
    print(f"{err}")

try:
    print(f"Testing healing_potion: {healing_potion()}")
except Exception as err:
    print(f"{err}")
