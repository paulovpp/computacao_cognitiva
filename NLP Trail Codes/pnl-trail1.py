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
# questions = pd.read_csv("socialmedia-disaster-tweets-DFE.csv", encoding='ansi', error_bad_lines=False)
# url = 'https://raw.githubusercontent.com/hundredblocks/concrete_NLP_tutorial/master/socialmedia_relevant_cols.csv'
# questions = pd.read_csv(url, encoding='ISO-8859-1', error_bad_lines=False)
questions = pd.read_csv("socialmedia_relevant_cols.csv", encoding='ISO-8859-1', error_bad_lines=False)
questions.columns=['text', 'choose_one', 'class_label']
# questions.columns=[]

#Primeiras linhas 
questions.head()
# print(questions.head())

#Últimas linhas 
questions.tail()
# print(questions.tail())

#Últimas linhas 
questions.describe()
print(questions.describe())

# Expressões regulares para limpeza dos dados 
def standardize_text(df, text_field):    
    df[text_field] = df[text_field].str.replace(r"http\S+", "")    
    df[text_field] = df[text_field].str.replace(r"http", "")    
    df[text_field] = df[text_field].str.replace(r"@\S+", "")    
    df[text_field] = df[text_field].str.replace(r"[^A-Za-z0-9(),!?@\'\`\"\_\n]", " ")    
    df[text_field] = df[text_field].str.replace(r"@", "at")    
    df[text_field] = df[text_field].str.lower()    
    return df

#Limpeza e regravação do arquivo de saída limpo 
clean_questions = standardize_text(questions, "text") 
clean_questions.to_csv("clean_data.csv")

#Primeiras linhas 
clean_questions.head()
#Últimas linhas 
clean_questions.tail()

clean_questions.groupby("class_label").count()

# Desassembling the data
from nltk.tokenize import RegexpTokenizer 
# Método de quebra dos dados 
tokenizer = RegexpTokenizer(r'\w+') 
# Gerando listas de sentenças quebradas 
clean_questions["tokens"] = clean_questions["text"].apply(tokenizer.tokenize)

#Primeiras linhas 
clean_questions.head()

#Últimas linhas 
clean_questions.tail()

#Inspecionando novamente os dados 
all_words = [word for tokens in clean_questions["tokens"] for word in tokens] 
sentence_lengths = [len(tokens) for tokens in clean_questions["tokens"]] 
VOCAB = sorted(list(set(all_words))) 
print("%s Quantidade total de palavras, com um vocabulário de %s" % (len(all_words), len(VOCAB))) 
print("Tamanho máximo de uma sentença %s" % max(sentence_lengths))

#Distribuição das sentenças por quantidade de palavras 
fig = plt.figure(figsize=(10, 10)) 
plt.xlabel('Tamanho da sentença') 
plt.ylabel('Número de sentenças') 
plt.hist(sentence_lengths) 
plt.show()