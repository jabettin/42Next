#!/usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import sys
import numpy as np
import requests


def api_call() -> None:
    try:
        r = requests.get("https://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?format=json&per_page=300&date=2022")
        data = r.json()
        print(type(data), len(data))
        print(data[0])
        print(data[1][:2])
    except ConnectionError as e:
        print(f"The module:  has not been installed {e}")
        continue()