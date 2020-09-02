import os
import string
import nltk
import re
import json
from nltk.stem.snowball import FrenchStemmer

stopword = nltk.corpus.stopwords.words('french')
stopword_cap = []
for i in stopword :
    stopword_cap.append(i.capitalize())
def remove_punct(text):
    string.punctuation += '’'
    text_nopunct = "".join([char for char in text if char not in string.punctuation])
    return text_nopunct
def tokenize(text) :
    tokens = re.split('\W+', text) 
    return tokens

def remove_stopwords(tokenized_list) :
    text = [word for word in tokenized_list if word not in stopword+stopword_cap]
    return text
stemmer = FrenchStemmer()
def stemming(tokenized_text) :
    text = [stemmer.stem(word) for word in tokenized_text]
    return text
def nlp(url) :
    root = "C:\\Users\\lenovo\\Downloads\\django\\myProject\\home\\"
    cell2 = url.replace('.txt','_clear.txt')
    f = open(root+url,"r",encoding="utf-8")
    f2 = open(root+"json\\" + cell2,"w",encoding="utf-8")
    for text in f :
        #print(text)
        text2 = remove_punct(text)
        f2.write(text2)
    f2.close()
    f.close()
    cell2 = url.replace('.txt','_clear.txt')
    cell3 = url.replace('.txt','_tokenized.json')
    cell4 = url.replace('.txt','_nostopwords.json')
    f = open(root+"json\\" + cell2,"r",encoding="utf-8")
    for text in f :
        #print(text)
        text2 = tokenize(text)
        #print(type(text2))
    with open(root+"json\\" + cell3,"w",encoding="utf-8") as f3 :
        json.dump(text2,f3,ensure_ascii=False)
    with open(root+"json\\" + cell3,"r",encoding="utf-8") as f3 :
        lists = json.load(f3)
        lists_no_stopwords = remove_stopwords(lists)
    with open(root+"json\\" + cell4,"w",encoding="utf-8") as f4 :
        json.dump(lists_no_stopwords,f4,ensure_ascii=False)
    with open(root+"json\\" + cell4,"r",encoding="utf-8") as f4 :
        lists_no_stopwords = json.load(f4)
    f.close()
    os.remove(root+"json\\" + cell3)
    os.remove(root+"json\\" + cell2)
    cell4 = url.replace('.txt','_nostopwords.json')
    cell5 = url.replace('.txt','_stemmed.json')
    with open(root+"json\\" + cell4,"r",encoding="utf-8") as f4 :
        lists_no_stopwords = json.load(f4)
        lists_stemmed = stemming(lists_no_stopwords)
        #print(lists_stemmed)
    with open(root+"json\\" + cell5,"w",encoding="utf-8") as f5 :
        json.dump(lists_stemmed,f5,ensure_ascii=False)
    with open(root+"json\\" + cell5,"r",encoding="utf-8") as f5 :
        lists_stemmed = json.load(f5)
    os.remove(root+"json\\" + cell4)
    cell_stemmed = "json\\" + url.replace('.txt','_stemmed.json')
    return cell_stemmed
