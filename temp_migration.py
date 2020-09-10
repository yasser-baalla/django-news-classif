import os as os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myProject.settings")
django.setup()
from home.models import category,category_info,temporary

articles = category.objects.all()
print(len(articles))
for i in range(1,len(articles)) : 
    article = category.objects.filter(id_cat=i)
    article_info = category_info.objects.filter(id_cat_info=i)
    article_info.article = article.article
    article.save()
