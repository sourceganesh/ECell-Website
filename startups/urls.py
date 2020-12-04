from django.urls import path,include
from startups import views

app_name = 'startups'
urlpatterns = [
    path('', views.indexView, name='index'),
]
