#!/usr/bin/env python3

import sys
import importlib


def import_handler() -> dict:
    accumulator = {}
    packages = [
        "pandas",
        "numpy",
        "matplotlib.pyplot",
        "requests"
    ]
    for module in packages:
        try:
            mod = importlib.import_module(module)
            accumulator[module] = mod
        except ImportError as e:
            print(f"{module} could not be loaded: {e}")
    return accumulator


def api_call(module: dict) -> None:
    try:
        r = requests.get("https://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?format=json&per_page=300&date=2022")
        r.raise_for_status()
        data = r.json()
        print(type(data), len(data))
        print(data[0])
        print(data[1][:2])
    except requests.exceptions.RequestException as e:
        print(f"Your API request has failed: {e}")
