import datetime
import requests

from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework import status

from api.v1.author.serializers import AuthorGetSerializer, AuthorPostSerializer
from author.models import Author
from main.functions import generate_serializer_errors, get_auto_id


@api_view(['GET'])
@permission_classes((AllowAny,))
@renderer_classes((JSONRenderer,))
def author_list(request):
    
    try :
        instances = Author.objects.filter(is_deleted=False)
        
        serialized = AuthorGetSerializer(instances, many=True, context={"request": request})
        
        status_code = status.HTTP_200_OK  
        response_data = {
            "status": status_code,
            "StatusCode": 6000,
            "data": serialized.data,
        }
    except :
        status_code = status.HTTP_400_BAD_REQUEST 
        response_data = {
            "status": status_code,
            "StatusCode": 6001,
        }

    return Response(response_data, status_code)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
@renderer_classes((JSONRenderer,))
def create_author(request):
    serialized = AuthorPostSerializer(data=request.data)
    
    if serialized.is_valid():
        serialized.save(
         auto_id = get_auto_id(Author),
         creator = request.user,
        )
        
        status_code = status.HTTP_200_OK
        response_data = {
            "status": status_code,
            "StatusCode": 6000,
            "data": serialized.data,
            "message": "Successfully created"
        }
    else:
        status_code = status.HTTP_400_BAD_REQUEST
        errors = generate_serializer_errors(serialized.errors)
        
        response_data = {
            "status": status_code,
            "StatusCode": 6001,
            "message": errors,
        }

    return Response(response_data, status=status_code)