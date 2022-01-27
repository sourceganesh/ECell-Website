from django.urls import path,include
from . import views

app_name='recruitment'

urlpatterns = [
    path('',views.index, name="index"),
    # path('management',views.management_form,name='management'),
    # path('media',views.media_form,name='media'),
    # path('web',views.web_form,name='web'),
]