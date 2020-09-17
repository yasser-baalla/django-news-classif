from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('page/',views.page, name='page'),
    path('id/', views.id, name='id'),
    path('view/', views.view, name='view')
]
