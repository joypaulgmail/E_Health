from django.urls import path
from . import views
urlpatterns=[
    path("doctoradd/", views.doctoradd),
    path('doctorsearch/',views.doctorsearch),
    path("doctordetail/",views.doctoretail),
    path("doctorsearchsubmit/",views.doctorsearchsubmit),
    path("doctorapoint/",views.doctorapoint),

]