from django.urls import path
from .views import *

urlpatterns = [
    # Address's CRUD
    path('create_address/', create_Address),  # All Address Fields and id_user
    path('<int:id_user>-get_address/', get_Address),  # id_user
    path('update_address/', update_Address),  # id_address , city , country , street
    path('delete_address/', delete_Address),  # id_address
]
