from django.urls import path,include
from podcasts import views


app_name='podcasts'
urlpatterns = [
    path('',views.index,name='index')
]

