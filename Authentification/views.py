import random

from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import api_view
from .models import *
from .serializer import UserSerializer


def generate_six_digit_id():
    return random.randint(100000, 999999)

@api_view(['POST'])
def create_User(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("User created successfully")
    return Response({"errors is not valid": serializer.errors}, status=400)

@api_view(['GET'])
def get_user(request,email):
    try:
        user = CustomUser.objects.get(email=email)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)
    except CustomUser.DoesNotExist:
        return Response("user does not exist")
    except Exception as e:
        return Response(str(e))
@api_view(['POST'])
def sendVerificationCode(request):
    if request.method == 'POST':
        data = request.data

        if 'email' not in data:
            return Response({"error": "Email is required."}, status=400)

        try:
            custom_user_instance = CustomUser.objects.get(email=data["email"])
            updateVerificationcode(ecommerce=custom_user_instance)

            subject = 'Your Verification Code'
            message = f'Your verification code is {custom_user_instance.verification_code}'
            from_email = 'znaidi2049@gmail.com'
            recipient_list = [data["email"]]

            send_mail(subject, message, from_email, recipient_list)

            return Response(f'Code sent to {data["email"]}')
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found."}, status=404)
        except CustomUser.DoesNotExist:
            return Response({"error": "Ecommerce user not found."}, status=404)


@api_view(['POST'])
def verifyVerificationCode(request):
    data = request.data
    ecommerce_instance = CustomUser.objects.get(email=data["email"])
    if ecommerce_instance.verification_code == data["verification_code"]:
        return Response("Verified!")
    else:
        return Response(status=400)

@api_view(['POST'])
def logout(request):
    try:
        refresh_token = request.data["refresh"]
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response({"message": "Successfully logged out."})
    except Exception as e:
        return Response({"error": str(e)})


def updateVerificationcode(ecommerce):
    ecommerce.verification_code = generate_six_digit_id()
    ecommerce.save()


@api_view(['POST'])
def resetPassword(request):
    data = request.data
    user_instance = CustomUser.objects.get(email=data["email"])
    if user_instance is not None:
        user_instance.password = make_password(data["new_password"])
        user_instance.save()
        return Response("Password has been reset")
    else:
        return Response("User not found")


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['id'] = user.id
        token['email'] = user.email
        token['user_image'] = user.user_image.url if user.user_image else None

        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['age_user'] = user.age_user
        token['num_tlfn'] = user.num_tlfn

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# Create your views here.
