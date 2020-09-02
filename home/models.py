from django.db import models
from django.core.validators import validate_comma_separated_integer_list
# Create your models here.




class category_info(models.Model):
    id_cat = models.CharField(primary_key=True, null=False,max_length=100)
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
    url = models.CharField(max_length = 100)
    id_cat= models.CharField(validators=[validate_comma_separated_integer_list],max_length=200, blank=True)
    pos_neg = models.CharField(max_length = 100)
    simp_comp = models.CharField(max_length = 100)
    title = models.CharField(max_length = 100)
    image = models.CharField(max_length = 100)

class temporary(models.Model):
    link = models.CharField(max_length = 100)
