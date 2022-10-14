"""group10_project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from re import template
from django.contrib import admin
from django.urls import path
#from group10_project1.views import hello_geek
from django.urls import include
from . import views
from .views import GeeksList

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('geek/', hello_geek), 
    #path('', include("myApp.urls")),
    #path('',views.index)
    #path('', views.home_view),
    #path('', views.formset_view)
    #path('', views.geeks_view),
    #path('', views.list_view),
    path('', GeeksList.as_view()),
    #path('', views.create_view),
    # path('<id>', views.detail_view),
    # path('<id>/update', views.update_view),
    # path('<id>/delete', views.delete_view ),

    # path('about/', views.MyView.as_view()),

    # #path('', views.GeeksCreate.as_view() ),
    # path('<pk>/', views.GeeksDetailView.as_view()),
    # path('<pk>/update', views.GeeksUpdateView.as_view()),
    # path('<pk>/delete/', views.GeeksDeleteView.as_view()),
    #path('', views.GeeksFormView.as_view()),

    path('geekswithfield/<id>', views.GeeksWithFiledList.as_view()),
    path('geekswithfield/', views.GeeksWithFieldCreate.as_view())
]
