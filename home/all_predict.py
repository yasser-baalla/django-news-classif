# -*- coding: utf-8 -*-
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
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.multiclass import OneVsRestClassifier
from cat_predict import *


def all_predict(link):

    cat_prediction = cat_predict(link)

    with open("pickled\\PN\\vectorizer.pickle", "rb") as f:
        pn_vectorizer = pickle.load(f)
    with open("pickled\\PN\\classifier.pickle", "rb") as f:
        pn_OVR = pickle.load(f)

    with open("pickled\\CS\\vectorizer.pickle", "rb") as f:
        cs_vectorizer = pickle.load(f)
    with open("pickled\\CS\\classifier.pickle", "rb") as f:
        cs_OVR = pickle.load(f)
    with open("pickled\\CS\\scaler.pickle", "rb") as f:
        cs_scaler = pickle.load(f)

    with open(link, "r", encoding="utf-8") as inp:
        X_manual = json.load(inp)
        X_manual_len = len(X_manual)
    X_manual = np.array(X_manual).reshape(1, -1)

    # complexe simple
    cs_X_manual = cs_vectorizer.transform(X_manual).toarray()
    X_manual_len = cs_scaler.transform(
        np.array(X_manual_len).reshape(-1, 1).astype(int))
    cs_X_manual = np.append(cs_X_manual[0], cat_prediction.toarray())
    cs_X_manual = np.append(cs_X_manual, X_manual_len)
    cs_prediction = cs_OVR.predict(cs_X_manual.reshape(1, -1))

    # positif negatif
    pn_X_manual = pn_vectorizer.transform(X_manual).toarray()
    pn_X_manual = np.append(pn_X_manual[0], cat_prediction.toarray())
    pn_prediction = pn_OVR.predict(pn_X_manual.reshape(1, -1))
    a = cat_prediction.toarray()
    id_cat =[]
    for i in range(1,a.shape[1]) :
        if a[0][i] == 1 :
            id_cat.append(i)
    pn = 2
    for i in range(pn_prediction[0].shape[0]) :
        if(pn_prediction[0][i] == 1) :
            pn = i
            break
    if(pn == 0) :
        pn = "positif"
    elif(pn == 1) :
        pn = "negatif"
    else : 
        pn = "neutre"
    #print(pn)
    cs = 1
    for i in range(cs_prediction[0].shape[0]) :
        if(cs_prediction[0][i] == 1) :
            cs = i
            break
    if(cs == 0) :
        cs = "complexe"
    else :
        cs = "simple"
    #print(cs)
    return id_cat,pn,cs
    





