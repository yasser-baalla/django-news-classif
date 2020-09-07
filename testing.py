import os as os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myProject.settings")
django.setup()


from home.models import temporary
f = open("C:\\Users\\lenovo\\Downloads\\django\\myProject\\les_articles_temp.txt",mode="a+")
q1 = temporary.objects.all()
for i in range(len(q1)) : 
    f.write(q1[i].link)
f.close()