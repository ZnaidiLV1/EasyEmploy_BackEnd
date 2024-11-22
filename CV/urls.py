from django.urls import path
from .views import *

urlpatterns = [
    # CV's CRUD
    path('create_cv/', create_cv),  # all fields and client_id
    path('<int:client_id>-get_cv/', get_cv),  # client_id
    path('update_cv/', update_cv),  # linkedIn_link , git_link , etablissement , diplome
    path('delete_cv/', delete_cv),  # cv_id
    # Experience's CRUD
    path('create_experience/', create_experience),  # all fields and cv_id
    path('<int:cv_id>-get_experiences/', get_experiences),  # cv_id
    path('update_experience/', update_Experience),  # exp_id and all fields
    path('delete_experience/', delete_Experience),  # exp_id
    # Diploma's CRUD
    path('create_diploma/', create_experience),  # all fields and cv_id
    path('<int:cv_id>-get_diplomas/', get_experiences),  # cv_id
    path('update_diploma/', update_Experience),  # dip_id and all fields
    path('delete_diploma/', delete_Experience),  # dip_id
]