from django.urls import path,include
from broadcast import views

app_name='broadcast'
urlpatterns = [
    path('',views.index,name='index')
]
