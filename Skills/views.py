from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *
from .models import *

@api_view(['POST'])
def create_skill(request):
    try:
        data = request.data
        skill = Skill.objects.create(
            name=data["name"]
        )
        serializer = skillSerializer(skill, many=False)
        return Response(serializer.data)
    except CV.DoesNotExist:
        return Response("cv does not exist")
    except Exception as e:
        return Response(str(e))

@api_view(['GET'])
def get_skills(request):
    skills=Skill.objects.all()
    serializer=skillSerializer(skills,many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def update_skill(request):
    try:
        data = request.data
        skill = Skill.objects.get(id=data["skill_id"])
        skill.name = data["name"]
        skill.save()
        serializer = skillSerializer(skill, many=False)
        return Response(serializer.data)
    except Skill.DoesNotExist:
        return Response("Skill does not exist")
    except Exception as e:
        return Response(str(e))

@api_view(['DELETE'])
def delete_skill(request):
    try:
        data = request.data
        skill = Skill.objects.get(id=data["skill_id"])
        skill.delete()
        return Response("Skill deleted")
    except Skill.DoesNotExist:
        return Response("Skill does not exist")
    except Exception as e:
        return Response(str(e))

# SkillPerCv
@api_view(['POST'])
def add_skills_to_cv(request):
    try:
        data=request.data
        cv = CV.objects.get(id=data["cv_id"])
        spc_list=[]
        for item in data["skills_list"]:
            skill = Skill.objects.get(id=item)
            spc = SkillPerCv.objects.create(
                cv_id=cv,
                skill_id=skill
            )
            spc_list.append(spc)
        serializer=spcSerializer(spc_list,many=True)
        return Response(serializer.data)
    except Skill.DoesNotExist:
        return Response("Skill does not exist")
    except Exception as e:
        return Response(str(e))

@api_view(['GET'])
def get_skills_cv(request,cv_id):
    try:
        skills_id = SkillPerCv.objects.filter(cv_id=cv_id).values_list("skill_id", flat=True)
        skills = Skill.objects.filter(id__in=skills_id).order_by('id')
        serializer = skillSerializer(skills, many=True)
        return Response(serializer.data)
    except SkillPerCv.DoesNotExist:
        return Response("SPC does not exist")
    except Exception as e:
        return Response(str(e))

@api_view(['DELETE'])
def delete_spc(request):
    try:
        data = request.data
        skill = SkillPerCv.objects.get(id=data["spc_id"])
        skill.delete()
        return Response("SPC deleted")
    except SkillPerCv.DoesNotExist:
        return Response("Skill does not exist")
    except Exception as e:
        return Response(str(e))
# Create your views here.
