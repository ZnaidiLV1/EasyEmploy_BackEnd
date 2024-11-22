from django.urls import path
from .views import *

# skill/ before every url
urlpatterns = [
    # Skill model urls
    path('create_skill/', create_skill),  # name
    path('get_skills/', get_skills),  # nothing
    path('update_skill/', update_skill),  # skill_id,name
    path('delete_skill/', delete_skill),  # skill_id
    # SkillPerCv
    path('add_skill_to_cv/', add_skills_to_cv),
    path('<int:cv_id>-get_skills/', get_skills_cv),  # cv_id,skills_list
    path('delete_spc/', delete_spc),  # spc_id
]
