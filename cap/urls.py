from django.urls import path,include
from cap import views

app_name = 'cap'
urlpatterns = [
    path('', views.index, name="index")
]