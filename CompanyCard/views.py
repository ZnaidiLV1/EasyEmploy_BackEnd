from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializer import *

@api_view(["POST"])
def create_companyCard(request):
    try:
        data = request.data
        user = CustomUser.objects.get(id=data["user_id"])
        company_card = CompanyCard.objects.create(
            user_id=user,
            street=data["street"],
            size=int(data["size"]),
            bio=data["bio"],
            employees_number=int(data["employees_number"]),
            establishment_date=datetime.strptime(data["date_fin"], "%d-%m-%Y").date(),
            git_link=data["git_link"],
            linkedIn_link=data["linked_in"],
            x_link=data["x_link"],
            website_link=data["website_link"]
        )
        serializer = companyCardserializer(company_card, many=False)
        return Response(serializer.data)
    except CustomUser.DoesNotExist:
        return Response("user does not exist")
    except CompanyCard.DoesNotExist:
        return Response("CompanyCard does not exist")
    except Exception as e:
        return Response(str(e))

@api_view(["GET"])
def get_companyCard(request,user_id):
    try:
        company_card = CompanyCard.objects.get(user_id=user_id)
        serializer = companyCardserializer(company_card, many=False)
        return Response(serializer.data)
    except CompanyCard.DoesNotExist:
        return Response("CompanyCard does not exist")
    except Exception as e:
        return Response(str(e))

@api_view(["PUT"])
def update_companyCard(request):
    try:
        data = request.data
        company_card = CompanyCard.objects.get(id=data["user_id"])
        company_card.street = data["street"],
        company_card.size = int(data["size"]),
        company_card.bio = data["bio"],
        company_card.employees_number = int(data["employees_number"]),
        company_card.establishment_date = datetime.strptime(data["date_fin"], "%d-%m-%Y").date(),
        company_card.git_link = data["git_link"],
        company_card.linkedIn_link = data["linked_in"],
        company_card.x_link = data["x_link"],
        company_card.website_link = data["website_link"]
        company_card.save()
        serializer = companyCardserializer(company_card, many=False)
        return Response(serializer.data)
    except CompanyCard.DoesNotExist:
        return Response("CompanyCard does not exist")
    except Exception as e:
        return Response(str(e))

@api_view(["DELETE"])
def delete_companyCard(request):
    try:
        data=request.data
        user = CustomUser.objects.get(id=data["id_user"])
        company_card = CompanyCard.objects.get(user_id=user.id)
        company_card.delete()
        return Response("company card deleted")
    except CustomUser.DoesNotExist:
        return Response("user does not exist")
    except CompanyCard.DoesNotExist:
        return Response("CompanyCard does not exist")
    except Exception as e:
        return Response(str(e))


# Create your views here.
