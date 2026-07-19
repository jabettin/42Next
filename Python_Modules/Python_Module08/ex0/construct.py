#!/usr/bin/env python3
import os
import sys
import site


def in_venv() -> bool:
    return sys.prefix != sys.base_prefix


def matrix_status(venv_active: bool) -> str:
    if venv_active:
        return "MATRIX STATUS: Welcome to the construct\n"
    else:
        return "MATRIX STATUS: You're still plugged in\n"


def path_status(venv_active: bool) -> str:
    if venv_active:
        return (
                f"Current Python: {sys.executable}\n"
                "Virtual environment: matrix_env\n"
                f"Environment path: {os.path.dirname(os.path.realpath(__file__))}\n"
                f"{sys.path[0]}"
        )
    else:
        return (
            f"Current Python: {sys.executable}\n"
            "Virtual environment: None detected"
        )


def matrix_instructions(venv_active: bool) -> str:
    if venv_active:
        return (
            "Package installation path\n"
            f"{site.getsitepackages()[0]}"
            
        )
    if not venv_active:
        return (
            "To enter the construct run:\n"
            "python -m venv matrix_env\n"
            "source matrix_env/bin/activate # On Unix\n"
            r"source matrix_env\scripts\activate # On Windows"
            "\n\n"
            "Then run this program again"
        )


def matrix():
    venv_active = in_venv()
    print()
    print(matrix_status(venv_active))
    print(path_status(venv_active))
    print(matrix_instructions(venv_active))


if __name__ == '__main__':
    matrix()
