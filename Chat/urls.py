# urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *
from Chat.views import *

urlpatterns = [
    path('<int:user1_id>/<int:user2_id>/', private_chat, name='private_chat'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
