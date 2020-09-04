# -*- coding: utf-8 -*-
# from home.polling import *
from home.scraping import *
from home.nlp import nlp
from home.all_predict import all_predict
def process_hespress(link,title) :
    link = link
    url,image = hespress(link)
    path = nlp(url)
    id_cat,pn,cs = all_predict(path)
    source = "hespress"
    return link,path,title,image,id_cat,pn,cs,source
def process_le360(link,title) :
    link = link
    url,image = le360(link)
    path = nlp(url)
    id_cat,posneg,comsim = all_predict(path)
    source = "le360"
    return link,path,title,image,id_cat,posneg,comsim,source
def process_afrique(link,title) :
    link = link
    url,image = afrique(link)
    path = nlp(url)
    id_cat,posneg,comsim = all_predict(path)
    source = "le360 afrique"
    return link,path,title,image,id_cat,posneg,comsim,source
def process_sport(link,title) :
    link = link
    url,image = sport(link)
    path = nlp(url)
    id_cat,posneg,comsim = all_predict(path)
    source = "le360 sport"
    return link,path,title,image,id_cat,posneg,comsim,source
def process_leseco(link,title) :
    link = link
    url,image = leseco(link)
    path = nlp(url)
    id_cat,posneg,comsim = all_predict(path)
    source = "lesEco"
    return link,path,title,image,id_cat,posneg,comsim,source
def process_welovebuzz(link,title) :
    link = link
    url,image = welovebuzz(link)
    path = nlp(url)
    id_cat,posneg,comsim = all_predict(path)
    source = "welovebuzz"
    return link,path,title,image,id_cat,posneg,comsim,source
