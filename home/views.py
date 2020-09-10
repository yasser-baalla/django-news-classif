from django.shortcuts import render, HttpResponse,HttpResponseRedirect,redirect
from django.http import JsonResponse
from django.contrib.sessions.models import Session
from django.views.decorators.csrf import csrf_exempt
from home.models import category, category_info, temporary
from home.polling import *
from home.scraping import *
from home.processing import *
import json
import time
import re
# Create your views here.

@csrf_exempt
def home(request):
    if request.method == "POST":
        myDict = json.loads(request.body)['cat']
        mySearch = json.loads(request.body)['search']
        #print(mySearch)
        mySearch = mySearch.lower()
        cat_search = ["politique","parlement","economie","tourisme","bourse","immobilier","société","rumeurs","statistiques","célébrité","divertissement","monde","culture","terrorisme","meteo","education","santé","covid","agriculture","espace","nature","animaux","religion","revue"]
        cat2_search = ["parties politiques","réseaux sociaux","local trends","eid el adha","revue de presse","revue du web"]
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
            if mySearch.strip() :
                cat_search = ["politique","parlement","economie","tourisme","bourse","immobilier","société","rumeurs","statistiques","célébrité","divertissement","monde","culture","terrorisme","meteo","education","santé","covid","agriculture","espace","nature","animaux","religion","revue"]
                cat2_search = ["parties politiques","réseaux sociaux","local trends","eid el adha","revue de presse","revue du web"]
                cat3_search = ["loi", "décret", "blessures","décès","accidents","histoire","football"]
                a_cat_temp = []
                mySearch = mySearch.strip()
                mySearch = list(mySearch.split(' '))
                list1 = []
                list2 = []
                i = 0
                while(i < len(mySearch)) :
                    if mySearch[i] in cat_search :
                        list1.append(mySearch[i])
                        i += 1
                    elif(i < len(mySearch)-1 and str(mySearch[i]+" "+mySearch[i+1]) in cat2_search) :
                        list1.append(str(mySearch[i]+" "+mySearch[i+1]))
                        i += 2
                    elif(i < len(mySearch)-2 and str(mySearch[i]+" "+mySearch[i+1]+" "+mySearch[i+2]) in cat2_search) :
                        list1.append(str(mySearch[i]+" "+mySearch[i+1]+" "+mySearch[i+2]))
                        i += 3
                    elif(mySearch[i] in cat3_search) :
                        list1.append(mySearch[i])
                        i += 1
                    else :
                        list2.append(mySearch[i])
                        i += 1
                list2 = list2 + list1
                a_cat2 = a_cat
                """
                1.separate words into list using ' ' separator
                2.using dict cat_search and other dicts separete into two lists : keyword list and search list
                ex : "sport messi local trends parties" => list1 = ["sport", "local trends"] and list2=["messsi", "parties"]
                3. code bellow will iterate on list1 --- DONE
                4.islike
                """
                for j in range(len(list1)) :
                    mySearch = list1[j]
                    for i in range(len(a_cat)) :
                        skip = 0
                        if( mySearch in cat_search ) :
                            a_cat[i] = category_info.objects.filter(id_cat_info=a_cat[i].id_cat_info).filter(**{mySearch : True})
                        elif( mySearch in cat2_search ) :
                            if(mySearch == "local trends") :
                                a_cat[i] = category_info.objects.filter(id_cat_info=a_cat[i].id_cat_info).filter(Local_Trends = True)
                            else :
                                mySearch.replace(" ","_")
                                a_cat[i] = category_info.objects.filter(id_cat_info=a_cat[i].id_cat_info).filter(**{mySearch : True})
                        elif( mySearch == "blessures" or mySearch == "décès" or mySearch == "accidents") :
                            a_cat[i] = category_info.objects.filter(id_cat_info=a_cat[i].id_cat_info).filter(blessures_accidents_et_décès=True)
                        elif( mySearch == "loi" or mySearch == "décret") :
                            a_cat[i] = category_info.objects.filter(id_cat_info=a_cat[i].id_cat_info).filter(loi_et_décret=True)
                        elif( mySearch == "histoire" or mySearch == "football") :
                            mySearch2 = mySearch.capitalize()
                            a_cat[i] = category_info.objects.filter(id_cat_info=a_cat[i].id_cat_info).filter(**{mySearch2 : True})
                        else : 
                            skip = 1
                        if skip :
                            pass
                        elif a_cat[i].count() == 0 :
                            a_cat[i] = "empty"
                        else :
                            a_cat[i] = a_cat[i][0]
                        if a_cat[i] != "empty" :
                            a_cat_temp.append(a_cat[i])
                    a_cat = a_cat_temp
                    a_cat_temp = []
                    print(type(a_cat))
                for j in range(len(list2)) :
                    mySearch2 = list2[j]
                    for i in range(len(a_cat2)) :
                        a_cat2[i] = category_info.objects.filter(id_cat_info=a_cat2[i].id_cat_info,article__contains=mySearch2)
                        if a_cat2[i].count() == 0 :
                            a_cat2[i] = "empty"
                        else :
                            a_cat2[i] = a_cat2[i][0]
                        if a_cat2[i] != "empty" :
                            a_cat2_temp.append(a_cat2[i])
                    a_cat2 = a_cat_temp
                # deletables = []
                # final_a_cat = a_cat + a_cat2
                # for i in range(len(final_a_cat)) : 
                #     if(final_a_cat.count(final_a_cat[i].id_cat_info))
        else :
            a_cat=categories
        final_articles = []
        for i in range(len(a_cat)) :
            final_articles.append(articles.filter(id_cat=a_cat[i].id_cat_info)[0])
        categories_final = []
        for i in range(len(a_cat)):
            a = []
            for attr, value in a_cat[i].__dict__.items():
                if value == True and attr != 'id_cat_info' :
                    a.append(attr)
            a.append(final_articles[i].pos_neg)
            a.append(final_articles[i].simp_comp)
            categories_final.append(a)
        data = '{ "articleList" : ['
        for i in range(min(12,len(final_articles))) :#*pages,12*pages+12)) : #*x,12*x+12) :
            var = '{"id" :"' + str(final_articles[i].id_cat) + '", "source":"' + final_articles[i].source + '","title":"' + final_articles[i].title.replace('"','') + '","date":"' + final_articles[i].date.strftime('%d/%m/%Y - %H:%M:%S') + '","content":"' + final_articles[i].url + '","image":"' + final_articles[i].image + '","cat":' + re.sub("([a-z])_([a-z])","\\1 \\2",str(categories_final[i]).replace("'",'"')) + '},'
            data = data + var
        if data == '{ "articleList" : [' :
            data = '{ "dataError" : true }'
        else :
            if(len(final_articles) % 12):
                pages = str(int(len(final_articles)/12 + 1))
            else :
                pages = str(int(len(final_articles)/12))
            request.session.create()
            request.session.set_expiry(1800)
            session_key = request.session.session_key
            print(session_key)
            # for i in range(len(final_articles)) :
            #     if type(final_articles[i]) != str :
            #         print("hey " + str(i) )
            #         print(type(final_articles[i]))
            request.session['final_articles'] = final_articles
            request.session['categories_final'] = categories_final
            data = data[:-1] + '] , "pages" : ' + str(int(len(final_articles)/12 + 1)) + ',"session_key" : "' + session_key + '"}'
        return JsonResponse(data, safe=False)
    else:
        return HttpResponse(status = 201)

@csrf_exempt
def page(request):
    #print(request.session.session_key)
    if request.method == "POST" :
        myPage = int(json.loads(request.body)['page']) - 1
        session_key = json.loads(request.body)['session_key']
        s = Session.objects.get(pk=session_key)
        session_data = s.get_decoded()
        final_articles = session_data['final_articles']
        categories_final = session_data['categories_final']
        data = '{ "articleList" : ['
        for i in range(12*myPage,min( 12*myPage + 12,len(final_articles))) :#*pages,12*pages+12)) : #*x,12*x+12) :
            var = '{"id" :"' + str(final_articles[i].id_cat) + '", "source":"' + final_articles[i].source + '","title":"' + final_articles[i].title.replace('"','') + '","date":"' + final_articles[i].date.strftime('%d/%m/%Y - %H:%M:%S') + '","content":"' + final_articles[i].url + '","image":"' + final_articles[i].image + '","cat":' + re.sub("([a-z])_([a-z])","\\1 \\2",str(categories_final[i]).replace("'",'"')) + '},'
            data = data + var
        data = data[:-1] + '] }'
        return JsonResponse(data, safe=False)
    else:
        return HttpResponse(status=201)
        # final_articles = request.session.get("final_articles")
        # print(final_articles)
        # pages = request.session.get("pages",1) - 1 
        # print(pages)
        # data = '{ "articleList" : ['
        # for i in range(12*pages,12*pages+12):
        #     var = '{"id" :"' + str(final_articles[i].id_cat) + '", "source":"' + final_articles[i].source + '","title":"' + final_articles[i].title.replace('"','') + '","date":"' + final_articles[i].date.strftime('%d/%m/%Y - %H:%M:%S') + '","content":"' + final_articles[i].url + '","image":"' + final_articles[i].image + '","cat":' + re.sub("([a-z])_([a-z])","\\1 \\2",str(categories_final[i]).replace("'",'"')) + '},'
        #     data = data + var
        # if data == '{ "articleList" : [' :
        #     data = '{ "dataError" : true }'
        # else :
        #     if(len(final_articles) % 12):
        #         pages = str(int(len(final_articles)/12 + 1))
        #     else :
        #         pages = str(int(len(final_articles)/12))
        #     data = data[:-1] + '] , "pages" : ' + str(int(len(final_articles)/12 + 1)) + ' }'
        # return JsonResponse(request, safe=False)
    
@csrf_exempt
def id(request):
    if request.method == "POST":
        id_value = json.loads(request.body)['id']
        articles = category.objects.filter(id_cat=id_value)
        if articles.count():
            articles = articles[0]
            return JsonResponse('{"article" : { "source" : "' + articles.source + '" , "content" : "' + articles.url + '" }}', safe=False)
        else:
            return JsonResponse('{"dataError": true}', safe=False)
    return HttpResponse(status=201)