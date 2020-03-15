import numpy as np
import pandas as pd
import math
import copy
from scipy import constants
import random

for i in range (0,100,1):
    decay = random.randint(1,10)
    if decay <= 1:
        break
    else:
        print(decay)