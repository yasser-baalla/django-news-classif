from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from home.models import category, category_info, temporary
from home.polling import *
from home.scraping import *
from home.processing import *
import json
import time
import re
# Create your views here.
# cat_dict = {
#     "1.0": "politique",
#     "2.0": "parties_politiques",
#     "3.0": "parlement",
#     "4.0": "Histoire",
#     "5.0": "economie",
#     "6.0": "tourisme",
#     "7.0": "bourse",
#     "8.0": "immobilier",
#     "9.0": "football",
#     "10.0": "société",
#     "11.0": "réseaux_sociaux",
#     "12.0": "rumeurs",
#     "13.0": "statistiques",
#     "14.0": "célébrité",
#     "15.0": "divertissement",
#     "16.0": "monde",
#     "17.0": "culture",
#     "18.0": "santé",
#     "19.0": "covid",
#     "20.0": "agriculture",
#     "21.0": "espace",
#     "22.0": "local_trends",
#     "23.0": "loi_décret",
#     "24.0": "nature",
#     "25.0": "animaux",
#     "26.0": "eid_el_adha",
#     "27.0": "terrorisme",
#     "28.0": "meteo",
#     "29.0": "revue_presse",
#     "30.0": "revue_web",
#     "31.0": "blessures",
#     "32.0": "education",
#     "33.0": "error",
#     "34.0": "sport",
#     "35.0": "science",
#     "36.0": "religion",
#     "37.0": "revue",
# }


@csrf_exempt
def home(request):
    if request.method == "POST":
        myDict = json.loads(request.body)['cat']
        mySearch = json.loads(request.body)['search']
        print(mySearch)
        mySearch = mySearch.lower()
        cat_search = ["politique","parlement","economie","tourisme","bourse","immobilier","société","rumeurs","statistiques","célébrité","divertissement","monde","culture","terrorisme","meteo","education","santé","covid","agriculture","espace","nature","animaux","religion","revue"]
        cat2_search = ["parties politiques","réseaux sociaux","local trends","eid el adha","revue de presse","revue du web"]
        if mySearch.strip() :
            if( mySearch in cat_search ) :
                if( mySearch == "politique") :
                    q1 = category_info.objects.filter(politique=True)
                    articles = []
                    for i in range(len(q1)) :
                        myId = q1[i].id_cat_info
                        articles.append(category.objects.filter(id_cat = myId))
                    articles = articles
                if( mySearch == "parlement") :
                    q1 = category_info.objects.filter(parlement=True)
                    articles = []
                    for i in range(len(q1)) :
                        myId = q1[i].id_cat_info
                        articles.append(category.objects.filter(id_cat = myId))
                    articles = articles
                if( mySearch == "economie") :
                    q1 = category_info.objects.filter(economie=True)
                    articles = []
                    for i in range(len(q1)) :
                        myId = q1[i].id_cat_info
                        articles.append(category.objects.filter(id_cat = myId))
                    articles = articles
                if( mySearch == "tourisme") :
                    q1 = category_info.objects.filter(politique=True)
                    articles = []
                    for i in range(len(q1)) :
                        myId = q1[i].id_cat_info
                        articles.append(category.objects.filter(id_cat = myId))
                    articles = articles
            elif( mySearch in cat2_search ) :
                if(mySearch == "local trends") :
                    mySearch.upper()
                    mySearch.replace(" ","_")
                    articles = category_info.objects.filter(mySearch=True).order_by('-date')
                else :
                    mySearch.replace(" ","_")
                    articles = category_info.objects.filter(mySearch=True)
            elif( mySearch == "blessures" or mySearch == "décès" or mySearch == "accidents") :
                articles = category_info.objects.filter(blessures_accidents_et_décès=True).order_by('-date')
            elif( mySearch == "loi" or mySearch == "décret") :
                articles = category_info.objects.filter(loi_et_décret=True).order_by('-category__date')
            elif( mySearch == "histoire" or mySearch == "football") :
                mySearch = mySearch.capitalise()
                articles = category_info.objects.filter(Histoire=True).order_by('-date')
            else : 
                articles = category.objects.order_by('-date')
        if 'tag' in myDict :
            field = myDict['tag']
            if(field == "sources") :
                articles = category.objects.order_by('-date')
            elif(field == "le360" or field == "lesEco" or field == "hespress" or field == "welovebuzz" or field == "le360 sport" or field == "le360 afrique") :
                articles = category.objects.filter(source=field).order_by('-date')
            elif(field == "complexe" or field == "simple") :
                articles = category.objects.filter(simp_comp=field).order_by('-date')
            elif(field == "positif" or field == "negatif" or field == "neutre") :
                articles = category.objects.filter(pos_neg=field).order_by('-date')
            else :
                field = "empty"
                articles = category.objects.order_by('-date')
        elif 'sources' in myDict :
            #----------------sources---------------
            blocked_sources = []
            for attr, value in myDict['sources'].items():
                if value == False :
                    blocked_sources.append(attr)
            articles = category.objects.order_by('-date')
            for obj in blocked_sources :
                articles = articles.exclude(source=obj)
            #-------------------------pos_neg---------------------
            blocked_sources = []
            for attr, value in myDict['émotion'].items():
                if value == False :
                    blocked_sources.append(attr)
            for obj in blocked_sources :
                articles = articles.exclude(pos_neg=obj)
            #---------------simp_comp---------
            blocked_sources = []
            for attr, value in myDict['complexité'].items():
                if value == False :
                    blocked_sources.append(attr)
            for obj in blocked_sources :
                articles = articles.exclude(simp_comp=obj)
        else :
            articles = category.objects.order_by('-date')
        categories = []
        for i in range(len(articles)) :
            categories.append(category_info.objects.filter(id_cat_info=articles[i].id_cat)[0])
        if 'tag' in myDict and field == "empty" :
            field = myDict['tag'].replace(" ","_")
            a_cat = []
            for i in range(len(categories)) :
                categories[i] = category_info.objects.filter(id_cat_info=categories[i].id_cat_info).filter(**{field : True})
                if categories[i].count() != 0 :
                    a_cat.append(categories[i][0])
        elif 'sources' in myDict :
            a_cat = []
            for i in range(len(categories)) :
                #-----------------cats-----------------
                for attr, value in myDict.items():
                    if attr not in ["sources","émotion","complexité"] :
                        #---------------dicts-------------
                        if type(value) == dict :
                            for dict_attr, dict_value in value.items():
                                if dict_value == False and categories[i] != "empty":
                                    a_dict_attr = dict_attr.replace(" ","_")
                                    categories[i] = category_info.objects.filter(id_cat_info=categories[i].id_cat_info).exclude(**{a_dict_attr : True})
                                    if categories[i].count() == 0 :
                                        categories[i] = "empty"
                                    else :
                                        categories[i] = categories[i][0]
                        else :
                            #---------------values-------------
                            if value == False and categories[i] != "empty":
                                a_attr = attr.replace(" ","_")
                                categories[i] = category_info.objects.filter(id_cat_info=categories[i].id_cat_info).exclude(**{a_attr : True })
                                if categories[i].count() == 0 :
                                    categories[i] = "empty"
                                else :
                                    categories[i] = categories[i][0]
                #-----------clear empty categories[i]----------
                if categories[i] != "empty" :
                    a_cat.append(categories[i])
        else :
            a_cat=categories
        final_articles = []
        for i in range(len(a_cat)) :
            final_articles.append(articles.filter(id_cat=a_cat[i].id_cat_info)[0])
        categories_final = []
        for i in range(len(a_cat)):
            a = []
            for attr, value in a_cat[i].__dict__.items():
                if value == True and attr != 'id_cat_info':
                    a.append(attr)
            a.append(final_articles[i].pos_neg)
            a.append(final_articles[i].simp_comp)
            categories_final.append(a)
        data = "["
        for i in range(len(final_articles)) :
            var = '{"source":"' + final_articles[i].source + '","title":"' + final_articles[i].title.replace('"','') + '","date":"' + final_articles[i].date.strftime('%d/%m/%Y - %H:%M:%S') + '","content":"' + final_articles[i].url + '","image":"' + final_articles[i].image + '","cat":' + re.sub("([a-z])_([a-z])","\\1 \\2",str(categories_final[i]).replace("'",'"')) + '},'
            data = data + var
        if data == "[" :
            data = '{ "dataError" : true }'
        else :
            data = data[:-1] + "]"
        return JsonResponse(data, safe=False)
    else:
        return render(request, 'test.html')


def home2(request):
    return JsonResponse({'foo': 'bar'})
