from django.urls import path
from .views import *

# announce/ before every url
urlpatterns = [
    # Announce's urls
    path('publier_announce/', publier_announce),  # user_id and all fields
    path('<int:user_id>-my_announces/', get_announces_publies),  # user_id
    path('<int:announce_id>-get_announce/', get_announce_x),  # announce_id
    path('all_announces/', get_all_announces),  # nothing to send in the request
    path('update_announce/', update_announce),  # announce_id , object, contenu
    path('update_is_checked/', update_isCheked_false),  # announce_id
    path('delete_announce/', delete_announce),  # announce_id
    # APC's urls
    path('postuler_announce/', postuler_announce),  # announce_id ,user_id
    path('<int:user_id>-listes_announce_postules/', get_user_announces_postules),  # user_id
    path('delete_postule_announce/', delete_announce_per_client),  # apc_id
    # SPA's urls
    path('add_skills_to_announce/',add_skills_to_announce),  # announce_id, skills_list
    path('<int:announce_id>-get_skills_announce/',get_skills_announce),  # announce_id
    path('delete_spa/',delete_spa),  # spa_id
]
