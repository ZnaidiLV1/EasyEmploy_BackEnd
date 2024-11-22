from django.urls import path
from .views import *

urlpatterns = [
    # CompanyCard'urls
    # entreprise/
    path('create_companyCard/', create_companyCard),  # all fields
    path('<int:user_id>-get_companyCard/', get_companyCard),  # user_id
    path('update_companyCard/', update_companyCard),  # all fields
    path('delete_company/', delete_companyCard)  # nothing
]
