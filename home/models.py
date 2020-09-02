from django.db import models

# Create your models here.




class category_info(models.Model):
    id_cat = models.CharField(primary_key=True)
    politique = models.BooleanField()
    parties_politiques = models.BooleanField()
    parlement = models.BooleanField()
    Histoire = models.BooleanField()
    economie = models.BooleanField()
    tourisme = models.BooleanField()
    bourse = models.BooleanField()
    immobilier = models.BooleanField()
    sport = models.BooleanField() 
    football = models.BooleanField()
    société = models.BooleanField() 
    réseaux_sociaux = models.BooleanField()
    santé = models.BooleanField() 
    covid = models.BooleanField()
    science = models.BooleanField() 
    agriculture = models.BooleanField() 
    espace = models.BooleanField()
    nature = models.BooleanField() 
    animaux = models.BooleanField()
    religion = models.BooleanField()
    eid_el_adha = models.BooleanField()
    revue = models.BooleanField() 
    revue_presse = models.BooleanField() 
    revue_web = models.BooleanField()
    rumeurs = models.BooleanField()
    statistiques = models.BooleanField()
    célébrité = models.BooleanField()
    divertissement = models.BooleanField()
    monde = models.BooleanField()
    culture = models.BooleanField()
    local_trends = models.BooleanField()
    loi_décret = models.BooleanField()
    terrorisme = models.BooleanField()
    meteo = models.BooleanField()
    blessures = models.BooleanField()
    education = models.BooleanField()

class category(models.Model):
    url = models.CharField()
    id_cat = models.ForeignKey(category_info, on_delete=models.CASCADE)
    pos_neg = models.CharField()
    simp_comp = models.CharField()
    title = models.CharField()
    image = models.CharField()

class temporary(models.Model):
    link = models.CharField()
