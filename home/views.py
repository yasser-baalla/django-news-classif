from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from home.models import category,category_info,temporary
from home.polling import *
from home.scraping import *
from home.processing import *
import json
import time
# Create your views here.
cat_dict = {
    "1.0" : "politique",
    "2.0" : "parties_politiques",
    "3.0" : "parlement",
    "4.0" : "Histoire",
    "5.0" : "economie",
    "6.0" : "tourisme",
    "7.0" : "bourse",
    "8.0" : "immobilier",
    "9.0" : "football",
    "10.0" : "société",
    "11.0" : "réseaux_sociaux",
    "12.0" : "rumeurs",
    "13.0" : "statistiques",
    "14.0" : "célébrité",
    "15.0" : "divertissement",
    "16.0" : "monde",
    "17.0" : "culture",
    "18.0" : "santé" ,
    "19.0" : "covid"  ,
    "20.0" : "agriculture", 
    "21.0" : "espace",
    "22.0" : "local_trends",
    "23.0" : "loi_décret",
    "24.0" : "nature" ,
    "25.0" : "animaux",
    "26.0" : "eid_el_adha",
    "27.0" : "terrorisme",
    "28.0" : "meteo",
    "29.0" : "revue_presse", 
    "30.0" : "revue_web",
    "31.0" : "blessures",
    "32.0" : "education",
    "33.0" : "error",
    "34.0" : "sport",
    "35.0" : "science",
    "36.0" : "religion",
    "37.0" : "revue",
}
@csrf_exempt
def home(request) :
    if request.method == "POST" :
        # print(json.loads(request.body))
        articles = category.objects.all()
        categories = category_infos.objects.all()
        categories_final = []
        for obj in categories :
            a = []
            for cat_list in obj :
                for attr, value in k.__dict__.items():
                    if value == True :
                        a.append(attr)
            categories_final.append(a)
        var = '''[{"source":"le360","title":"'Ensam A7san mdrassa' - ki goul Ennaji","date":"Aout 14, 2020    16:04","content":"https://le360.com/ki_goul_ennaji","image":"https://www.doyoubuzz.com/var/users/_/2013/2/2/12/436687/avatar/458976/avatar_cp_big.jpg?t=1597246065","cat":["simple","positif","le360","célébrité","education"]}]'''
        return JsonResponse(var,safe=False)
    else :
        return render(request, 'test.html')

def home2(request) :
    return JsonResponse({'foo':'bar'})