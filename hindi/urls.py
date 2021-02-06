from django.urls import path
from . import views
urlpatterns=[
    path("", views.search),
    path("addmovie/",views.addmovie),
    path("add_hospital/",views.add_hospital),
    path("result/",views.result),
    path("search/", views.search),
    path("healthlibrary/",views.health_library),
]