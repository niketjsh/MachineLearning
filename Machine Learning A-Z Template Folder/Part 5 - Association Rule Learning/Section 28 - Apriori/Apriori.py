# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 09:05:34 2019

@author: Niket
"""

# Apriori


# Importing the library
import numpy as np
import matplotlib as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)
transactions = []
for i in range(0, 7501):
    transactions.append([str(dataset.values[i,j]) for j in range(0, 20)])

# Training Apriori on the dataset
from apyori import apriori
rules = apriori(transactions, min_support = 0.0028, min_confidence = 0.2, min_lift = 3, min_Length = 2)

# Visualising the results
results = list(rules)
print (results)

