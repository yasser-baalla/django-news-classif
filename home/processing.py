# -*- coding: utf-8 -*-
# from home.polling import *
from home.scraping import *
from home.nlp import nlp
from home.all_predict import all_predict
def process_hespress(link,title) :
    link = link
    url,image,article = hespress(link)
    path = nlp(url)
    id_cat,pn,cs = all_predict(path)
    for i in range(0,len(id_cat)) :
        if(id_cat[i] == 2 or id_cat[i] == 3 or id_cat[i] == 4) :
            id_cat.append(1)
        if(id_cat[i] == 6 or id_cat[i] == 7 or id_cat[i] == 8) :
            id_cat.append(5)
        if(id_cat[i] == 9) :
            id_cat.append(34)
        if(id_cat[i] == 20 or id_cat[i] == 21) :
            id_cat.append(35)
        if(id_cat[i] == 25) :
            id_cat.append(24)
        if(id_cat[i] == 26) :
            id_cat.append(36)
        if(id_cat[i] == 29 or id_cat[i] == 30) :
            id_cat.append(37)
    for i in range(0,len(id_cat)) :
        if(id_cat.count(id_cat[i]) == 2) :
            id_cat.remove(id_cat[i])
    source = "hespress"
    return link,path,title,image,id_cat,pn,cs,source,article
def process_le360(link,title) :
    link = link
    url,image,article = le360(link)
    path = nlp(url)
    id_cat,posneg,comsim = all_predict(path)
    for i in range(len(id_cat)) :
        if(id_cat[i] == 2 or id_cat[i] == 3 or id_cat[i] == 4) :
            id_cat.append(1)
        if(id_cat[i] == 6 or id_cat[i] == 7 or id_cat[i] == 8) :
            id_cat.append(5)
        if(id_cat[i] == 9) :
            id_cat.append(34)
        if(id_cat[i] == 20 or id_cat[i] == 21) :
            id_cat.append(35)
        if(id_cat[i] == 25) :
            id_cat.append(24)
        if(id_cat[i] == 26) :
            id_cat.append(36)
        if(id_cat[i] == 29 or id_cat[i] == 30) :
            id_cat.append(37)
    for i in range(0,len(id_cat)) :
        if(id_cat.count(id_cat[i]) == 2) :
            id_cat.remove(id_cat[i])
    source = "le360"
    return link,path,title,image,id_cat,posneg,comsim,source,article
def process_afrique(link,title) :
    link = link
    url,image,article = afrique(link)
    path = nlp(url)
    id_cat,posneg,comsim = all_predict(path)
    for i in range(len(id_cat)) :
        if(id_cat[i] == 2 or id_cat[i] == 3 or id_cat[i] == 4) :
            id_cat.append(1)
        if(id_cat[i] == 6 or id_cat[i] == 7 or id_cat[i] == 8) :
            id_cat.append(5)
        if(id_cat[i] == 9) :
            id_cat.append(34)
        if(id_cat[i] == 20 or id_cat[i] == 21) :
            id_cat.append(35)
        if(id_cat[i] == 25) :
            id_cat.append(24)
        if(id_cat[i] == 26) :
            id_cat.append(36)
        if(id_cat[i] == 29 or id_cat[i] == 30) :
            id_cat.append(37)
    for i in range(0,len(id_cat)) :
        if(id_cat.count(id_cat[i]) == 2) :
            id_cat.remove(id_cat[i])
    source = "le360 afrique"
    return link,path,title,image,id_cat,posneg,comsim,source,article
def process_sport(link,title) :
    link = link
    url,image,article = sport(link)
    path = nlp(url)
    id_cat,posneg,comsim = all_predict(path)
    for i in range(len(id_cat)) :
        if(id_cat[i] == 2 or id_cat[i] == 3 or id_cat[i] == 4) :
            id_cat.append(1)
        if(id_cat[i] == 6 or id_cat[i] == 7 or id_cat[i] == 8) :
            id_cat.append(5)
        if(id_cat[i] == 9) :
            id_cat.append(34)
        if(id_cat[i] == 20 or id_cat[i] == 21) :
            id_cat.append(35)
        if(id_cat[i] == 25) :
            id_cat.append(24)
        if(id_cat[i] == 26) :
            id_cat.append(36)
        if(id_cat[i] == 29 or id_cat[i] == 30) :
            id_cat.append(37)
    for i in range(0,len(id_cat)) :
        if(id_cat.count(id_cat[i]) == 2) :
            id_cat.remove(id_cat[i])
    source = "le360 sport"
    return link,path,title,image,id_cat,posneg,comsim,source,article
def process_leseco(link,title) :
    link = link
    url,image,article = leseco(link)
    path = nlp(url)
    id_cat,posneg,comsim = all_predict(path)
    for i in range(len(id_cat)) :
        if(id_cat[i] == 2 or id_cat[i] == 3 or id_cat[i] == 4) :
            id_cat.append(1)
        if(id_cat[i] == 6 or id_cat[i] == 7 or id_cat[i] == 8) :
            id_cat.append(5)
        if(id_cat[i] == 9) :
            id_cat.append(34)
        if(id_cat[i] == 20 or id_cat[i] == 21) :
            id_cat.append(35)
        if(id_cat[i] == 25) :
            id_cat.append(24)
        if(id_cat[i] == 26) :
            id_cat.append(36)
        if(id_cat[i] == 29 or id_cat[i] == 30) :
            id_cat.append(37)
    for i in range(0,len(id_cat)) :
        if(id_cat.count(id_cat[i]) == 2) :
            id_cat.remove(id_cat[i])
    source = "lesEco"
    return link,path,title,image,id_cat,posneg,comsim,source,article
def process_welovebuzz(link,title) :
    link = link
    url,image,article = welovebuzz(link)
    path = nlp(url)
    id_cat,posneg,comsim = all_predict(path)
    for i in range(len(id_cat)) :
        if(id_cat[i] == 2 or id_cat[i] == 3 or id_cat[i] == 4) :
            id_cat.append(1)
        if(id_cat[i] == 6 or id_cat[i] == 7 or id_cat[i] == 8) :
            id_cat.append(5)
        if(id_cat[i] == 9) :
            id_cat.append(34)
        if(id_cat[i] == 20 or id_cat[i] == 21) :
            id_cat.append(35)
        if(id_cat[i] == 25) :
            id_cat.append(24)
        if(id_cat[i] == 26) :
            id_cat.append(36)
        if(id_cat[i] == 29 or id_cat[i] == 30) :
            id_cat.append(37)
    for i in range(0,len(id_cat)) :
        if(id_cat.count(id_cat[i]) == 2) :
            id_cat.remove(id_cat[i])
    source = "welovebuzz"
    return link,path,title,image,id_cat,posneg,comsim,source,article
