import sys

print("REAGENT STATUS: Loading reagents...")
print("Checking dependencies:")

dependency: bool = True
pd_err: str = ""
np_err: str = ""

try:
    import pandas as pd
    pd_ver: str = pd.__version__
    print(f"[OK] pandas ({pd_ver}) - Data manipulation ready")
except ImportError as err:
    pd_err = str(err)
    dependency = False

try:
    import numpy as np
    np_ver: str = np.__version__
    print(f"[OK] numpy ({np_ver}) - Numerical computation ready")
except ImportError as err:
    np_err = str(err)
    dependency = False

if not dependency:
    if pd_err:
        print(f"[ERROR] pandas - {pd_err}")
    if np_err:
        print(f"[ERROR] nympy - {np_err}")
    print("Your laboratory is either empty or not sealed properly.")
    print("To install using pip (inside your sealed laboratory), run:")
    print("    pip install -r ex0/requirements.txt")
    print("    source ex0/lab_env/bin/activate")
    print("To install using Poetry (which seals the laboratory automatically), run:")
    print("    poetry install")
    sys.exit(1)
else:
    print("pip vs Poetry:")
    print("  requirements.txt declares what to install; pip resolves it at install time.")
    print("  pyproject.toml declares the same constraints, and Poetry pins the resolved")
    print("  versions in poetry.lock so every install is identical.")
    print("All reagents present and accounted for.")
