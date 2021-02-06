from django.urls import path
from . import views
urlpatterns=[
    path("sendrequest/",views.sendrequest),
    path("sendcoodinate/",views.sendcordinate),

    path("sendlocation/",views.sendlocation),

]