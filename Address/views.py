from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *


@api_view(['POST'])
def create_Address(request):
    address = addressSerializer(data=request.data)
    if address.is_valid():
        address.save()
        return Response("Address created successfully")
    else:
        return Response(address.errors, status=400)

@api_view(['GET'])
def get_Address(request, user_id):
    try:
        address=Address.objects.get(user_address=user_id)
        serializer=addressSerializer(address,many=False)
        return Response(serializer.data)
    except Address.DoesNotExist:
        return Response("Address Does not Exist")
    except Exception as e:
        return Response(str(e))

@api_view(['PUT','POST'])
def update_Address(request):
    try:
        data = request.data
        address = Address.objects.get(id=data["id_address"])

        address.country = request.data.get('country', address.country)
        address.city = request.data.get('city', address.city)
        address.street = request.data.get('street', address.street)

        address.save()
        return Response({"message": "Address updated successfully"}, )

    except Address.DoesNotExist:
        return Response({"error": "Address not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)})


@api_view(['DELETE','POST'])
def delete_Address(request, ):
    try:
        data = request.data
        address = Address.objects.get(id=data["id_address"])

        address.delete()
        return Response({"message": "Address deleted successfully"}, status=status.HTTP_200_OK)

    except Address.DoesNotExist:
        return Response({"error": "Address not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)})

# Create your views here.
