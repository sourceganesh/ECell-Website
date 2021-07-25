"""ecellwebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogs/',include('blogs.urls', namespace = 'blogs')),
    path('cap/',include('cap.urls', namespace = 'cap')),
    path('',include('core.urls', namespace = 'core')),
    path('courses/',include('courses.urls', namespace = 'courses')),
    path('startups/',include('startups.urls', namespace = 'startups')),
    path('team/',include('team.urls', namespace = 'team')),
    path('podcasts/',include('podcasts.urls', namespace = 'podcasts')),
    path('broadcast/',include('broadcast.urls', namespace = 'broadcast')),
    path('recruitment/',include('recruitment.urls', namespace='recruitment'))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
