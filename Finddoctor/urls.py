from django.urls import path
from Finddoctor import views
urlpatterns=[
    path('searchdoctor/',views.finddoctor),
    path('adddoctor/',views.adddoctor),
    path('bedbook/',views.bedbook),
]