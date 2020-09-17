import os as os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myProject.settings")
django.setup()

from home.models import category, category_info, temporary
from datetime import datetime
import time
import json,unicodedata
from home.processing import *
from home.scraping import *
from home.polling import *

def strip_accents(s) :
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn' )

cat_dict = {
    "1": "politique",
    "2": "parties_politiques",
    "3": "parlement",
    "4": "Histoire",
    "5": "economie",
    "6": "tourisme",
    "7": "bourse",
    "8": "immobilier",
    "9": "sport",
    "10": "Football",
    "11": "société",
    "12": "réseaux_sociaux",
    "13": "rumeurs",
    "14": "statistiques",
    "15": "célébrité",
    "16": "divertissement",
    "17": "monde",
    "18": "culture",
    "19": "santé",
    "20": "covid",
    "21": "science",
    "22": "agriculture",
    "23": "espace",
    "24": "Local_Trends",
    "25": "loi_et_décret",
    "26": "nature",
    "27": "animaux",
    "28": "religion",
    "29": "eid_el_adha",
    "30": "terrorisme",
    "31": "meteo",
    "32": "revue_de_presse",
    "33": "revue_du_web",
    "34": "blessures_accidents_et_décès",
    "35": "education",
    "36": "error",
    "37": "revue"
}
while True:
    try:
        link, title = sport360_polling()
        q1 = category.objects.filter(url=link)
        q3 = category.objects.filter(title=title)
        q2 = temporary.objects.filter(link=link)
        if(q1.count() != 0 or q2.count() != 0 or q3.count() != 0):
            print("Waiting for Messi...")
            time.sleep(60)
        else:
            link, path, title, image, id_cat, posneg, comsim, source, article = process_sport(
                link, title)
            article = article.lower()
            article = strip_accents(article)
            db_cat = []
            if(bool(id_cat) == False):
                base_db = temporary(link=link)
                base_db.save()
                print("the le360sport data has been written to the temp db")
            else:
                for i in range(len(id_cat)):
                    db_cat.append(cat_dict[str(id_cat[i])])
                base_db = category(
                    url=link, pos_neg=posneg, simp_comp=comsim, title=title, image=image, source=source, views=0)
                cat_db = category_info()
                for i in range(len(db_cat)):
                    setattr(cat_db, db_cat[i], True)
                    article = article + " " + db_cat[i].replace("_"," ").lower()
                title = title.lower()
                title = strip_accents(title)
                cat_db.article = title + " " + article
                base_db.save()
                cat_db.save()
                print("the le360sport data has been written to the db")
    except:
        with open("logs.txt", mode="a+") as f:
            f.write(datetime.today().strftime('[%Y-%m-%d-%H:%M:%S]'))
            f.write("from sport : ")
            for i in sys.exc_info():
                f.write(str(i))
            f.write("\n")
            print("""
            
            
            
            
            
            error occured from sport360
            
            
            
            
            """)
        time.sleep(60)
