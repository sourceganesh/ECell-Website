from django.urls import path,include
from startups import views

app_name = 'startups'
urlpatterns = [
    path('', views.index, name='index'),
]
