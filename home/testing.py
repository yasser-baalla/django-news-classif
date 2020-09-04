field = myDict['tag']
if(field == "sources") :
    pass
elif(field == "le360" or field == "lesEco" or field == "hespress" or field == "welovebuzz" or field == "le360 sport" or field == "le360 afrique") :
    articles = category.objects.filter(source=field).order_by('-date')
elif(field == "complexe" or field == "simple") :
    articles = category.objects.filter(simp_com=field).order_by('-date')
elif(field == "positif" or field == "negatif" or field == "neutre") :
    articles = category.objects.filter(pos_neg=field).order_by('-date')