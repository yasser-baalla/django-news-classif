from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from home import models
import json
# Create your views here.
@csrf_exempt
def home(request) :
    if request.method == "POST" :
        print(json.loads(request.body))
        var = '''[{"source":"le360","title":"'Ensam A7san mdrassa' - ki goul Ennaji","date":"Aout 14, 2020    16:04","content":"https://le360.com/ki_goul_ennaji","image":"https://www.doyoubuzz.com/var/users/_/2013/2/2/12/436687/avatar/458976/avatar_cp_big.jpg?t=1597246065","cat":["simple","positif","le360","célébrité","education"]},{"source":"welovebuzz","title":"Yasser Baalla : 'ana a7san l3ab d lkora ou li ma 3jbou 7al'","date":"Aout 12, 2020    18:36","content":"https://welovebuzz.com/yasser_baalla","image":"https://scontent.fcmn2-2.fna.fbcdn.net/v/t1.0-9/20882062_881541558669982_4788438431407912129_n.jpg?_nc_cat=110&_nc_sid=09cbfe&_nc_ohc=yMKPIgda6MIAX8FDU50&_nc_ht=scontent.fcmn2-2.fna&oh=e814e852d94bd76bbd060bf6c3f82e4f&oe=5F592650","cat":["simple","negatif","welovebuzz","célébrité","sport","football"]},{"source":"hespress","title":"Othmani : khourjo tsaraw bach drbou m3akou 350 DH l wa7ed","date":"Aout 12, 2020    07:29","content":"https://hespress.com/Othmani","image":"https://cdn.telquel.ma/content/uploads/2017/09/Capture-d%E2%80%99e%CC%81cran-2017-09-15-a%CC%80-11.33.23.png","cat":["simple","neutre","covid","politique","celebrité"]}]'''
        return JsonResponse(var,safe=False)
    else :
        return render(request, 'test.html')

def home2(request) :
    return JsonResponse({'foo':'bar'})