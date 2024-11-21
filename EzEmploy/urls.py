
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',include("Authentification.urls")),
    path('address/', include("Address.urls")),
    path('cv/', include("CV.urls")),
    path('announce/',include("Announce.urls")),
    path('skill/',include("Skills.urls")),
    path('chat/',include("Chat.urls")),
    path('field/',include("Fields.urls")),
    path('entreprise/',include("CompanyCard.urls"))
]
