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


def api_call(modules: dict) -> None:
    requests_module = modules.get("requests")
    if requests_module is None:
        print("requests unavailable, unable to fetch data")
        return
    try:
        r = requests_module.get("https://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?format=json&per_page=300&date=2022")
        r.raise_for_status()
        data = r.json()
    except requests_module.exceptions.RequestException as e:
        print(f"Your API request has failed: {e}")
        return
    return data[1]

def fallback_data_gen() -> list:
    country_names = [
        "The Netherlands",
        "Germany",
        "Belgium",
        "UK",
        "France",
        "Switzerland",
        "Poland"
    ]
    countries = {}
    generated_pop = numpy.random.randint(10000000000, size=(125, 1))
    for names, pop in enumerate(country_names):
        countries[country_names] = generated_pop
        print(names, pop)


def data_validator() -> None:
    
