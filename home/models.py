from django.db import models
# Create your models here.


class category(models.Model):
    url = models.CharField(max_length = 300)
    id_cat= models.AutoField( primary_key=True, null=False)
    pos_neg = models.CharField(max_length = 100)
    simp_comp = models.CharField(max_length = 100)
    title = models.CharField(max_length = 300)
    image = models.CharField(max_length = 300)
    source = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

class category_info(models.Model):
    id_cat_info = models.AutoField( primary_key=True, null=False)
    politique = models.BooleanField(default=False)
    parties_politiques = models.BooleanField(default=False)
    parlement = models.BooleanField(default=False)
    Histoire = models.BooleanField(default=False)
    economie = models.BooleanField(default=False)
    tourisme = models.BooleanField(default=False)
    bourse = models.BooleanField(default=False)
    immobilier = models.BooleanField(default=False)
    sport = models.BooleanField(default=False) 
    Football = models.BooleanField(default=False)
    société = models.BooleanField(default=False) 
    réseaux_sociaux = models.BooleanField(default=False)
    santé = models.BooleanField(default=False) 
    covid = models.BooleanField(default=False)
    science = models.BooleanField(default=False) 
    agriculture = models.BooleanField(default=False) 
    espace = models.BooleanField(default=False)
    nature = models.BooleanField(default=False) 
    animaux = models.BooleanField(default=False)
    religion = models.BooleanField(default=False)
    eid_el_adha = models.BooleanField(default=False)
    revue = models.BooleanField(default=False) 
    revue_de_presse = models.BooleanField(default=False) 
    revue_du_web = models.BooleanField(default=False)
    rumeurs = models.BooleanField(default=False)
    statistiques = models.BooleanField(default=False)
    célébrité = models.BooleanField(default=False)
    divertissement = models.BooleanField(default=False)
    monde = models.BooleanField(default=False)
    culture = models.BooleanField(default=False)
    Local_Trends = models.BooleanField(default=False)
    loi_et_décret = models.BooleanField(default=False)
    terrorisme = models.BooleanField(default=False)
    meteo = models.BooleanField(default=False)
    blessures_accidents_et_décès = models.BooleanField(default=False)
    education = models.BooleanField(default=False)
    article = models.CharField(max_length=10000)


class temporary(models.Model):
    link = models.CharField(max_length = 300)
