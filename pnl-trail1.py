'''
NPL Introduction trail

1. Starting by cleaning up the data, we will now look at the data in more detail.
2. Collecting data
3. Data cleaning
4. Data exploration
5. Data visualization 

'''

import keras
import nltk
import pandas as pd
import numpy as np
import re
import codecs
import itertools
import matplotlib
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
import gensim

# Inspecionando os dados 
questions = pd.read_csv("socialmedia-disaster-tweets-DFE.csv", encoding='ansi', error_bad_lines=False)
# questions.columns=['text', 'choose_one', 'class_label']
# questions.columns=[]

print(questions.head())

print(questions.tail())
