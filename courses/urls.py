from django.urls import path,include
from courses import views

app_name = 'courses'
urlpatterns = [
    path('', views.index, name='index'),
    path('entrepreneurship/', views.entrepreneurship, name="entrepreneurship"),
    path('finance/', views.finance, name="finance"),
    path('cryptocurrency/', views.cryptocurrency, name="cryptocurrency"),
    path('productManagement/', views.productManagement, name="productManagement"),
    path('entrepreneurship2/', views.entrepreneurship2, name="entrepreneurship2"),
]
