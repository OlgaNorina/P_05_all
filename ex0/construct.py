import sys
import os
import site


def check_env() -> None:
    """Detect Python environment status and print details."""
    is_venv: bool = (
            sys.prefix != sys.base_prefix or hasattr(sys, "real_prefix")
    )
    current_python: str

    if not is_venv:
        current_python = os.path.realpath(sys.executable)
        print("LABORATORY STATUS: You are working in the open")
        print(f"\nCurrent Python: {current_python}")
        print("Virtual Environment: None detected")
        print("\nWARNING: You are in the global environment!")
        print("Every reagent you install here leaks into the whole system.\n")
        print("To seal the laboratory, run:")
        print("python3 -m venv lab_env")
        print("source lab_env/bin/activate # On Unix")
        print("lab_env\\Scripts\\activate # On Windows")
        print("\nThen run this program again")
    else:
        current_python = sys.executable
        env_path: str = sys.prefix
        env_name: str = os.path.basename(env_path)
        site_packages: str = site.getsitepackages()[0]

        
        print("LABORATORY STATUS: The laboratory is sealed")
        print(f"\nCurrent Python: {current_python}")
        print(f"Virtual Environment: {env_name}")
        print(f"Environment Path: {env_path}\n")
        print("\nSUCCESS: You are working in an isolated environment!")
        print("Safe to install reagents without affecting")
        print("the global system.\n")
        print("\nReagent installation path:")
        print(site_packages)


if __name__ == "__main__":
    check_env()

