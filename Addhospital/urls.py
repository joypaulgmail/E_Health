from django.urls import path
from . import views
urlpatterns=[
    path("addhospital/",views.addhospital),
    path('hospitalsubmit/',views.hospitalsubmit),
    path('bloodsubmit/',views.bloodsubmit),
]