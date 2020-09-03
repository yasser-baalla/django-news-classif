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
@csrf_exempt
def home(request) :
    while True :
        link,title = hespress_polling()
        q1 = category.objects.filter(url=link,title=title)
        if(q1.count() != 0) :
            time.sleep(60)
        else :
            link,path,title,image,id_cat,posneg,comsim = process_hespress(link,title)
            a = category(url=link,id_cat=id_cat,pos_neg=posneg,simp_comp=comsim,title=title,image=image)
            a.save()
            print("the hespress data has been written to the db")
            time.sleep(60)
        link,title = afrique360_polling()
        q2 = category.objects.filter(url=link)
        q3 = category.objects.filter(title=title)
        if(q2.count() != 0 or q3.count() != 0) :
            time.sleep(60)
        else :
            link,path,title,image,id_cat,posneg,comsim = process_afrique(link,title)
            a = category(url=link,id_cat=id_cat,pos_neg=posneg,simp_comp=comsim,title=title,image=image)
            a.save()
            print("the afrique data has been written to the db")
            time.sleep(60)
        link,title = le360_polling()
        q4 = category.objects.filter(url=link)
        q5 = category.objects.filter(title=title)
        if(q4.count() != 0 or q5.count() != 0) :
            time.sleep(60)
        else :
            link,path,title,image,id_cat,posneg,comsim = process_le360(link,title)
            a = category(url=link,id_cat=id_cat,pos_neg=posneg,simp_comp=comsim,title=title,image=image)
            a.save()
            print("the 360 data has been written to the db")
            time.sleep(60)
        link,title = sport360_polling()
        q6 = category.objects.filter(url=link)
        q7 = category.objects.filter(title=title)
        if(q6.count() != 0 or q7.count() != 0) :
            time.sleep(60)
        else :
            link,path,title,image,id_cat,posneg,comsim = process_sport(link,title)
            a = category(url=link,id_cat=id_cat,pos_neg=posneg,simp_comp=comsim,title=title,image=image)
            a.save()
            print("the sport data has been written to the db")
            time.sleep(60)
        link,title = welovebuzz_polling()
        q8 = category.objects.filter(url=link,title=title)
        if(q8.count() != 0 ) :
            time.sleep(60)
        else :
            link,path,title,image,id_cat,posneg,comsim = process_welovebuzz(link,title)
            a = category(url=link,id_cat=id_cat,pos_neg=posneg,simp_comp=comsim,title=title,image=image)
            a.save()
            print("the welovebuzz data has been written to the db")
            time.sleep(60)
        link,title = leseco_polling()
        q8 = category.objects.filter(url=link,title=title)
        if(q8.count() != 0 ) :
            time.sleep(60)
        else :
            link,path,title,image,id_cat,posneg,comsim = process_leseco(link,title)
            a = category(url=link,id_cat=id_cat,pos_neg=posneg,simp_comp=comsim,title=title,image=image)
            a.save()
            print("the leseco data has been written to the db")
            time.sleep(60)
    if request.method == "POST" :
        print(json.loads(request.body))
        var = '''[{"source":"le360","title":"'Ensam A7san mdrassa' - ki goul Ennaji","date":"Aout 14, 2020    16:04","content":"https://le360.com/ki_goul_ennaji","image":"https://www.doyoubuzz.com/var/users/_/2013/2/2/12/436687/avatar/458976/avatar_cp_big.jpg?t=1597246065","cat":["simple","positif","le360","célébrité","education"]},{"source":"welovebuzz","title":"Yasser Baalla : 'ana a7san l3ab d lkora ou li ma 3jbou 7al'","date":"Aout 12, 2020    18:36","content":"https://welovebuzz.com/yasser_baalla","image":"https://scontent.fcmn2-2.fna.fbcdn.net/v/t1.0-9/20882062_881541558669982_4788438431407912129_n.jpg?_nc_cat=110&_nc_sid=09cbfe&_nc_ohc=yMKPIgda6MIAX8FDU50&_nc_ht=scontent.fcmn2-2.fna&oh=e814e852d94bd76bbd060bf6c3f82e4f&oe=5F592650","cat":["simple","negatif","welovebuzz","célébrité","sport","football"]},{"source":"hespress","title":"Othmani : khourjo tsaraw bach drbou m3akou 350 DH l wa7ed","date":"Aout 12, 2020    07:29","content":"https://hespress.com/Othmani","image":"https://cdn.telquel.ma/content/uploads/2017/09/Capture-d%E2%80%99e%CC%81cran-2017-09-15-a%CC%80-11.33.23.png","cat":["simple","neutre","covid","politique","celebrité"]}]'''
        return JsonResponse(var,safe=False)
    else :
        return render(request, 'test.html')

def home2(request) :
    return JsonResponse({'foo':'bar'})