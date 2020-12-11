from django.urls import path,include
from team import views

app_name="team"
urlpatterns = [
    path('', views.index, name='index')
]

