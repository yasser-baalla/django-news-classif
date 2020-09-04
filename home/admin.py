from django.contrib import admin
from home.models import category,category_info,temporary
# Register your models here.

admin.site.register(category)
admin.site.register(category_info)
admin.site.register(temporary)