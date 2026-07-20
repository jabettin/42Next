#!/usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import sys
import numpy as np
import requests


def api_call() -> None:
    r = requests.get()