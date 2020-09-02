# -*- coding: utf-8 -*-
from polling import *
from nlp import nlp
from all_predict import all_predict
def process_hespress(link,title) :
    link = link
    url,image = hespress(link)
    path = nlp(url)
    id_cat,pn,cs = all_predict(path)
    return link,path,title,image,id_cat,pn,cs
def process_le360(link,title) :
    link = link
    url,image = le360(link)
    path = nlp(url)
    id_cat,posneg,comsim = all_predict(path)
    return link,path,title,image,id_cat,posneg,comsim
def process_afrique(link,title) :
    link = link
    url,image = afrique(link)
    path = nlp(url)
    id_cat,posneg,comsim = all_predict(path)
    return link,path,title,image,id_cat,posneg,comsim
def process_sport(link,title) :
    link = link
    url,image = sport(link)
    path = nlp(url)
    id_cat,posneg,comsim = all_predict(path)
    return link,path,title,image,id_cat,posneg,comsim
def process_leseco(link,title) :
    link = link
    url,image = leseco(link)
    path = nlp(url)
    id_cat,posneg,comsim = all_predict(path)
    return link,path,title,image,id_cat,posneg,comsim
def process_welovebuzz(link,title) :
    link = link
    url,image = welovebuzz(link)
    path = nlp(url)
    id_cat,posneg,comsim = all_predict(path)
    return link,path,title,image,id_cat,posneg,comsim
