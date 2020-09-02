#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import os
import pickle
import pandas as pd
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
import scipy
import numpy as np
import json
from sklearn.naive_bayes import GaussianNB
from skmultilearn.problem_transform import ClassifierChain
from sklearn.preprocessing import MinMaxScaler


# In[2]:

def cat_predict(link):
    root = "C:\\Users\\lenovo\\Downloads\\django\\myProject\\home\\"
    with open(root+'pickled\\CC\\scaler.pickle', 'rb') as f:
        scaler = pickle.load(f)
    with open(root+'pickled\\CC\\vectorizer.pickle', 'rb') as f:
        vectorizer = pickle.load(f)
    with open(root+'pickled\\CC\\classifier.pickle', 'rb') as f:
        CC = pickle.load(f)
    with open(root+'pickled\\CC\\scaler2.pickle', 'rb') as f:
        scaler2 = pickle.load(f)
    # with open('pickled\\CC\\encoder.pickle', 'rb') as f :
    #     mlb = pickle.load(f)

    # In[3]:

    with open(root+link, "r", encoding="utf-8") as inp:
        X_manual = json.load(inp)
        X_manual_len = len(X_manual)
    X_num_digit = 0
    for string in X_manual:
        X_num_digit += sum(c.isdigit() for c in string)
    X_manual = np.array(X_manual).reshape(1, -1)
    X_manual = vectorizer.transform(X_manual).toarray()
    X_manual_len = scaler.transform(
        np.array(X_manual_len).reshape(-1, 1).astype(int))
    X_num_digit = scaler2.transform(
        np.array(X_num_digit).reshape(-1, 1).astype(int))
    X_manual = np.append(X_manual[0], X_manual_len)
    X_manual = np.append(X_manual, X_num_digit)
    # count = 0
    # for i in X_manual[0] :
    #     if i != 0. :
    #         count += 1
    # print(count)

    # In[4]:

    prediction2 = CC.predict(X_manual)
    return prediction2
