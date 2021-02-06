from django.urls import path
from . import views
urlpatterns=[
   # path("", views.search),
    #path("search/", views.search),
    path("",views.blood_required),
    path("bloodrequiredsubmit/",views.bloodrequired_submit),
    path("blooddonate/",views.blood_donate),
    path("blooddonatesubmit/",views.blood_donate_submit),
  ]