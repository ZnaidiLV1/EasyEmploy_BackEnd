from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *


@api_view(['POST'])
def create_cv(request):
    try:
        data = request.data
        client = CustomUser.objects.get(id=data["client_id"])
        cv = CV.objects.create(
            client_id=client,
            professional_level=data["professional_level"],
            salary=int(data["salary"]),
            bio=data["bio"],
            x_link=data["x_link"],
            linkedIn_link=data["linkedIn_link"],
            git_link=data["git_link"],
            portfolio_link=data["portfolio_link"],
            soft_life_description=data["soft_life_description"],
        )
        serializer = cvserializer(cv, many=False)
        return Response(serializer.data)
    except Exception as e:
        return Response(str(e))


@api_view(['GET'])
def get_cv(request, client_id):
    try:
        cv = CV.objects.get(client_id=client_id)
        serializer = cvserializer(cv, many=False)
        return Response(serializer.data)
    except CV.DoesNotExist:
        return Response("CV does not exist")
    except Exception as e:
        return Response(str(e))


@api_view(['PUT'])
def update_cv(request):
    try:
        data = request.data
        cv = CV.objects.get(id=data["id_cv"])
        cv.professional_level = data["professional_level"],
        cv.salary = int(data["salary"]),
        cv.bio = data["bio"],
        cv.x_link = data["x_link"],
        cv.linkedIn_link = data["linkedIn_link"],
        cv.git_link = data["git_link"],
        cv.portfolio_link = data["portfolio_link"],
        cv.soft_life_description = data["soft_life_description"],
        cv.save()
        serializer = cvserializer(cv, many=False)
        return Response(serializer.data)
    except CV.DoesNotExist:
        return Response("CV does not exist")
    except Exception as e:
        return Response(str(e))


@api_view(['DELETE', 'POST'])
def delete_cv(request):
    try:
        data = request.data
        cv = CV.objects.get(id=data["cv_id"])
        cv.delete()
        return Response("CV Deleted")
    except CV.DoesNotExist:
        return Response("CV does not exist")
    except Exception as e:
        return Response(str(e))


# Experience
@api_view(['POST'])
def create_experience(request):
    try:
        data = request.data
        cv = CV.objects.get(id=data["cv_id"])
        experience = Experience.objects.create(
            client_cv=cv,
            titre=data["titre"],
            lieu=data["lieu"],
            date_debut=datetime.strptime(data["date_debut"], "%d-%m-%Y").date(),
            date_fin=datetime.strptime(data["date_fin"], "%d-%m-%Y").date(),
            description=data["description"]
        )
        serializer = experienceserializer(experience, many=False)
        return Response(serializer.data)
    except Exception as e:
        return Response(str(e))


@api_view(['GET'])
def get_experiences(request, cv_id):
    try:
        cv = Experience.objects.filter(cv_id=cv_id)
        serializer = experienceserializer(cv, many=True)
        return Response(serializer.data)
    except Experience.DoesNotExist:
        return Response("Experience does not exist")
    except Exception as e:
        return Response(str(e))


@api_view(['PUT', 'POST'])
def update_Experience(request):
    try:
        data = request.data
        exp = Experience.objects.get(id=data["exp_id"])
        exp.titre = data["titre"]
        exp.lieu = data["lieu"]
        exp.date_debut = datetime.strptime(data["date_debut"], "%d-%m-%Y").date()
        exp.date_fin = datetime.strptime(data["date_fin"], "%d-%m-%Y").date()
        exp.description = data["description"]
        exp.save()
        serializer = experienceserializer(exp, many=False)
        return Response(serializer.data)
    except Experience.DoesNotExist:
        return Response("Experience does not exist")
    except Exception as e:
        return Response(str(e))


@api_view(['DELETE', 'POST'])
def delete_Experience(request):
    try:
        data = request.data
        exp = Experience.objects.get(id=data["exp_id"])
        exp.delete()
        return Response("Experience Deleted")
    except Experience.DoesNotExist:
        return Response("CV does not exist")
    except Exception as e:
        return Response(str(e))


# Diploma
@api_view(['POST'])
def create_diploma(request):
    try:
        data = request.data
        cv = CV.objects.get(id=data["cv_id"])
        experience = Experience.objects.create(
            client_cv=cv,
            titre=data["titre"],
            university=data["university"],
            date_debut=datetime.strptime(data["date_debut"], "%d-%m-%Y").date(),
            date_fin=datetime.strptime(data["date_fin"], "%d-%m-%Y").date(),
            current=data.get("current", "False").lower() in ['true', '1', 'yes']

        )
        serializer = diplomaserializer(experience, many=False)
        return Response(serializer.data)
    except Exception as e:
        return Response(str(e))


@api_view(['GET'])
def get_diplomas(request, cv_id):
    try:
        diploma = Diploma.objects.filter(cv_id=cv_id)
        serializer = diplomaserializer(diploma, many=True)
        return Response(serializer.data)
    except Diploma.DoesNotExist:
        return Response("Experience does not exist")
    except Exception as e:
        return Response(str(e))


@api_view(['PUT','POST'])
def update_diploma(request):
    try:
        data = request.data
        exp = Diploma.objects.get(id=data["dip_id"])
        exp.titre = data["titre"]
        exp.university = data["university"]
        exp.date_debut = datetime.strptime(data["date_debut"], "%d-%m-%Y").date()
        exp.date_fin = datetime.strptime(data["date_fin"], "%d-%m-%Y").date()
        exp.current = data.get("current", "False").lower() in ['true', '1', 'yes']
        exp.save()
        serializer = diplomaserializer(exp, many=False)
        return Response(serializer.data)
    except Diploma.DoesNotExist:
        return Response("Experience does not exist")
    except Exception as e:
        return Response(str(e))


@api_view(['DELETE','POST'])
def delete_diploma(request):
    try:
        data = request.data
        exp = Diploma.objects.get(id=data["dip_id"])
        exp.delete()
        return Response("Experience Deleted")
    except Diploma.DoesNotExist:
        return Response("CV does not exist")
    except Exception as e:
        return Response(str(e))


# Create your views here.
