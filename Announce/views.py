
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Skills.serializer import skillSerializer
from .serializer import *

@api_view(['POST'])
def publier_announce(request):
    try:
        data = request.data
        user = CustomUser.objects.get(id=data["user_id"])
        announce = Announce.objects.create(
            user_id=user,
            object=data["title"],
            required_level=data["required_level"],
            position_type=data["position_type"],
            contenu=data["contenu"],
            address=data["address"],
            type_announce=data.get("type_announce", "False").lower() in ['true', '1', 'yes'],
            places_disponibles=int(data["places_disponibles"])
        )
        serializer = announceSerializer(announce, many=False)
        return Response(serializer.data)
    except CustomUser.DoesNotExist:
        return Response("User does not exist")
    except Exception as e:
        return Response(str(e))

@api_view(['GET'])
def get_announces_publies(request,user_id):
    try:
        announces = Announce.objects.filter(user_id=user_id)
        serializer = announceSerializer(announces, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response(str(e))


@api_view(['GET'])
def get_announce_x(request,announce_id):
    try:
        announces = Announce.objects.get(id=announce_id)
        serializer = announceSerializer(announces, many=False)
        return Response(serializer.data)
    except Announce.DoesNotExist:
        return Response("Announce does not exist")
    except Exception as e:
        return Response(str(e))

@api_view(['GET'])
def get_all_announces(request):
    try:
        announces=Announce.objects.filter(is_checked=True)
        serializer=announceSerializer(announces,many=True)
        return Response(serializer.data)
    except Announce.DoesNotExist:
        return Response("Announces does not exist")
    except Exception as e:
        return Response(str(e))

@api_view(['PUT'])
def update_announce(request):
    try:
        data=request.data
        announces = Announce.objects.get(id=data["announce_id"])
        announces.title = data["title"],
        announces.required_level = data["required_level"],
        announces.position_type = data["position_type"],
        announces.contenu = data["contenu"],
        announces.address = data["address"],
        announces.places_disponibles = int(data["places_disponibles"])
        announces.save()
        serializer = announceSerializer(announces, many=False)
        return Response(serializer.data)
    except Announce.DoesNotExist:
        return Response("Announce does not exist")
    except Exception as e:
        return Response(str(e))

@api_view(['PUT'])
def update_isCheked_false(request):
    try:
        data=request.data
        announces = Announce.objects.get(id=data["announce_id"])
        announces.is_checked=False
        announces.save()
        serializer = announceSerializer(announces, many=False)
        return Response(serializer.data)
    except Announce.DoesNotExist:
        return Response("Announces does not exist")
    except Exception as e:
        return Response(str(e))

@api_view(['DELETE'])
def delete_announce(request):
    try:
        data=request.data
        announces=Announce.objects.get(id=data["announce_id"])
        announces.delete()
        return Response("Announce deleted")
    except Announce.DoesNotExist:
        return Response("Announce does not exist")
    except Exception as e:
        return Response(str(e))

# Announce Per Client
@api_view(['POST'])
def postuler_announce(request):
    try:
        data = request.data
        announce = Announce.objects.get(id=data["announce_id"])
        user = CustomUser.objects.get(id=data["user_id"])
        announcePerClient = AnnouncePerUser.objects.create(
            announce_id=announce,
            user_id=user,
        )
        serializer = announcePerUserSerializer(announcePerClient, many=False)
        return Response(serializer.data)
    except Announce.DoesNotExist:
        return Response("Announce does not exist")
    except CustomUser.DoesNotExist:
        return Response("User does not exist")
    except Exception as e:
        return Response(str(e))

@api_view(['GET'])
def get_user_announces_postules(request,user_id):
    try:
        announces_list=AnnouncePerUser.objects.filter(user_id=user_id).values_list("announce_id",flat=True)
        announces=Announce.objects.filter(id__in=announces_list)
        serializer=announceSerializer(announces,many=True)
        return Response(serializer.data)
    except AnnouncePerUser.DoesNotExist:
        return Response("Announce does not exist")
    except Exception as e:
        return Response(str(e))

@api_view(['DELETE'])
def delete_announce_per_client(request):
    try:
        data=request.data
        announce=AnnouncePerUser.objects.get(id=data["apc_id"])
        announce.delete()
        return Response("APC deleted")
    except AnnouncePerUser.DoesNotExist:
        return Response("Announce does not exist")
    except Exception as e:
        return Response(str(e))

# SkillPerAnnounce
@api_view(['POST'])
def add_skills_to_announce(request):
    try:
        data=request.data
        announce = Announce.objects.get(id=data["announce_id"])
        spa_list=[]
        for item in data["skills_list"]:
            skill = Skill.objects.get(id=item)
            spc = SkillPerAnnounce.objects.create(
                announce_id=announce,
                skill_id=skill
            )
            spa_list.append(spc)
        serializer=spaSerializer(spa_list,many=True)
        return Response(serializer.data)
    except Skill.DoesNotExist:
        return Response("Skill does not exist")
    except Exception as e:
        return Response(str(e))

@api_view(['GET'])
def get_skills_announce(request,announce_id):
    try:
        skills_id = SkillPerAnnounce.objects.filter(announce_id=announce_id).values_list("skill_id", flat=True)
        skills = Skill.objects.filter(id__in=skills_id).order_by('id')
        serializer = skillSerializer(skills, many=True)
        return Response(serializer.data)
    except SkillPerAnnounce.DoesNotExist:
        return Response("SPC does not exist")
    except Exception as e:
        return Response(str(e))

@api_view(['DELETE'])
def delete_spa(request):
    try:
        data = request.data
        skill = SkillPerAnnounce.objects.get(id=data["spa_id"])
        skill.delete()
        return Response("SPA deleted")
    except SkillPerAnnounce.DoesNotExist:
        return Response("SPA does not exist")
    except Exception as e:
        return Response(str(e))
# Create your views here.
