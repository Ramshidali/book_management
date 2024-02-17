import datetime
import requests
from api.v1.authentication.serializers import LogInSerializer, UserSerializer, UserTokenObtainPairSerializer
from main.functions import generate_serializer_errors

from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, renderer_classes


class UserTokenObtainPairView(TokenObtainPairView):
    serializer_class = UserTokenObtainPairSerializer

@api_view(['POST'])
@permission_classes((AllowAny,))
@renderer_classes((JSONRenderer,))
def register(request):
    serialized = UserSerializer(data=request.data)

    if serialized.is_valid():
        serialized.save()
        
        status_code = status.HTTP_201_CREATED
        response_data = {
            "StatusCode": status_code,
            "data": serialized.data,
            "message": "Registration Completed"
        }
    else:
        status_code = status.HTTP_400_BAD_REQUEST
        response_data = {
            "StatusCode": status_code,
            "message": generate_serializer_errors(serialized._errors)
        }
    return Response(response_data, status=status_code)
    
@api_view(['POST'])
@permission_classes((AllowAny,))
@renderer_classes((JSONRenderer,))
def login(request):
    serialized = LogInSerializer(data=request.data)

    if serialized.is_valid():

        username = serialized.data['username']
        password = serialized.data['password']

        headers = {
            'Content-Type': 'application/json',
        }
        
        data = '{"username": "' + username + '", "password":"' + password + '"}'
        protocol = "http://"
        if request.is_secure():
            protocol = "https://"

        web_host = request.get_host()
        request_url = protocol + web_host + "/api/v1/authentication/token/"

        response = requests.post(request_url, headers=headers, data=data)
        
        if response.status_code == 200:
            response_data = {
                "status": status.HTTP_200_OK,
                "StatusCode": 6000,
                "data": response.json(),
                "message": "Login successfully",
                
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            response_data = {
                "status": status.HTTP_401_UNAUTHORIZED,
                "StatusCode": 6001,
                "message": "Invalid username or password",
            }

            return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)
    else:
        response_data = {
            "status": status.HTTP_400_BAD_REQUEST,
            "StatusCode": 6001,
            "message": generate_serializer_errors(serialized._errors)
        }
        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)