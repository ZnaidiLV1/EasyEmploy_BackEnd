
from django.urls import path
from .views import *

urlpatterns = [
    # Fields's urls
    # field/
    path('create_field/',create_field),#name
    path('<int:field_id>-get_field/',get_field),
    path('update_field/',update_field),#name
    path('delete_field/',delete_field),
    #
]