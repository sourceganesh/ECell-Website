from django.urls import path,include
from courses import views

app_name = 'courses'
urlpatterns = [
    path('', views.indexView, name='index'),
    path('entrepreneurship/', views.entrepreneurship, name="entrepreneurship"),
    path('finance/', views.finance, name="finance"),
    path('cryptocurrency/', views.cryptocurrency, name="cryptocurrency"),
]
