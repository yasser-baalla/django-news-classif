import os as os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myProject.settings")
django.setup()

from home.polling import *
from home.scraping import *
from home.processing import *
import json
import time
from datetime import datetime
from home.models import category, category_info, temporary

cat_dict = {
    "1": "politique",
    "2": "parties_politiques",
    "3": "parlement",
    "4": "Histoire",
    "5": "economie",
    "6": "tourisme",
    "7": "bourse",
    "8": "immobilier",
    "9": "football",
    "10": "société",
    "11": "réseaux_sociaux",
    "12": "rumeurs",
    "13": "statistiques",
    "14": "célébrité",
    "15": "divertissement",
    "16": "monde",
    "17": "culture",
    "18": "santé",
    "19": "covid",
    "20": "agriculture",
    "21": "espace",
    "22": "local_trends",
    "23": "loi_décret",
    "24": "nature",
    "25": "animaux",
    "26": "eid_el_adha",
    "27": "terrorisme",
    "28": "meteo",
    "29": "revue_presse",
    "30": "revue_web",
    "31": "blessures",
    "32": "education",
    "33": "error",
    "34": "sport",
    "35": "science",
    "36": "religion",
    "37": "revue",
}

while True:
    try:
        link, title = afrique360_polling()
        q1 = category.objects.filter(url=link)
        q3 = category.objects.filter(title=title)
        q2 = temporary.objects.filter(link=link)
        if(q1.count() != 0 or q2.count() != 0 or q3.count() != 0):
            print("Waiting for africa...")
            time.sleep(60)
        else:
            link, path, title, image, id_cat, posneg, comsim, source, article = process_afrique(
                link, title)
            db_cat = []
            if(bool(id_cat) == False):
                base_db = temporary(link=link)
                base_db.save()
                print("the afrique data has been written to the temp db")
            else:
                for i in range(len(id_cat)):
                    db_cat.append(cat_dict[str(id_cat[i])])
                base_db = category(
                    url=link, pos_neg=posneg, simp_comp=comsim, title=title, image=image, source=source, article=article)
                cat_db = category_info()
                for i in range(len(db_cat)):
                    setattr(cat_db, db_cat[i], True)
                base_db.save()
                cat_db.save()
                print("the afrique data has been written to the db")
    except:
        with open("logs.txt", mode="a+") as f:
            f.write(datetime.today().strftime('[%Y-%m-%d-%H:%M:%S]'))
            f.write("from afrique : ")
            for i in sys.exc_info():
                f.write(str(i))
            f.write("\n")
            print("""
            
            
            
            
            
            error occured from afrique360
            
            
            
            
            """)
        time.sleep(60)
