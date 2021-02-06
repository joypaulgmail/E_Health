from django.urls import path ,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls .static import static




urlpatterns = [
    #path('admin/',admin.site.urls),
    path('',include("hindi.urls")),
    path('adddoctor/',include("Add_doctor.urls")),
    path('bloodbank/',include("Bloodbank.urls")),
    path('ambulence/',include('Ambulence.urls')),
    path('finddoctor/',include('Finddoctor.urls')),
    path('hospital/',include('Addhospital.urls')),
    path('doctor/',include("Doctor.urls"))
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
