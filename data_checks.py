# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 17:40:21 2020

@author: jfang
"""

import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

handwriting = pd.read_csv("A_Z Handwritten Data.csv", header=None)

#sanity checks
print(handwriting.iloc[500])
print(handwriting[0].value_counts())

#visualisation checks
#first_letter_labelled = handwriting.iloc[0]
#first_label = first_letter_labelled[0]
#first_letter = first_letter_labelled[1:]

#first_array = np.reshape(list(first_letter), (28, 28))

#fig = plt.figure(figsize = (3,3))
#ax = fig.add_subplot(3,3,1)
#ax.imshow(first_array, cmap = plt.cm.binary)
#plt.show()

#visualising a small sample of letters from the dataset
fig = plt.figure(figsize=(10, 12))

for i in range(30):
    letter_labelled = handwriting.iloc[i * 12000]
    letter = letter_labelled[1:]
    array = np.reshape(list(letter), (28, 28))
    ax = fig.add_subplot(5, 6, i+1)
    ax.imshow(array, plt.cm.binary)

plt.show
    