
from django.urls import path
from .views import *

urlpatterns = [
    # Fields's urls
    # field/
    path('create_field/',create_field),#name
    path('<int:field_id>-get_field/',get_field),
    path('update_field/',update_field),#name
    path('delete_field/',delete_field),
    # CvPerField'urls
    path('create_cvPerField/',create_cvPerField),#field_id,cv_id
    path('<int:cv_id>-get_cvFields/',get_cvFields),#cv_id
    path('delete_cvPerField/',delete_cvPerField),#field_id,cv_id
    # CompanyCardPerField'urls
    path('create_CompanyPerField/',create_ccpf),#companyCard_id,field_id
    path('<int:companyCard_id>-get_companyCardFields/',get_companyCardFields),
    path('delete_companyCardPerField/',delete_ccpf),#ccpf_id
]