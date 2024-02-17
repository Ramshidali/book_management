import datetime
import requests

from django.db.models import Avg

from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework import status

from book.models import Book, Review
from main.functions import generate_serializer_errors, get_auto_id
from api.v1.book.serializers import BookReviewSerializer, BookSerializer


@api_view(['GET'])
@permission_classes((AllowAny,))
@renderer_classes((JSONRenderer,))
def book_list(request):
    
    try :
        instances = Book.objects.filter(is_deleted=False)
        
        serialized = BookSerializer(instances, many=True, context={"request": request})
        
        status_code = status.HTTP_200_OK  
        response_data = {
            "status": status_code,
            "data": serialized.data,
        }
    except :
        status_code = status.HTTP_400_BAD_REQUEST 
        response_data = {
            "status": status_code,
        }

    return Response(response_data, status_code)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
@renderer_classes((JSONRenderer,))
def create_book(request):
    serialized = BookSerializer(data=request.data)
    
    if serialized.is_valid():
        serialized.save(
         auto_id = get_auto_id(Book),
         creator = request.user,
        )
        
        status_code = status.HTTP_200_OK
        response_data = {
            "status": status_code,
            "data": serialized.data,
            "message": "Successfully created"
        }
    else:
        status_code = status.HTTP_400_BAD_REQUEST
        errors = generate_serializer_errors(serialized.errors)
        
        response_data = {
            "status": status_code,
            "message": errors,
        }

    return Response(response_data, status=status_code)


@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
@renderer_classes((JSONRenderer,))
def update_book(request,pk):
    try:
        book_instance = Book.objects.get(pk=pk)

        serializer = BookSerializer(book_instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            
            status_code = status.HTTP_200_OK
            response_data = {
                "status": status_code,
                "data": serializer.data,
                "message": "Updated successfully.",
            }
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            response_data = {
                "status": status_code,
                "errors": serializer.errors,
            }
    except Book.DoesNotExist:
        status_code = status.HTTP_404_NOT_FOUND
        response_data = {
            "status": status_code,
            "message": "Not found.",
        }
    return Response(response_data, status=status_code)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
@renderer_classes((JSONRenderer,))
def delete_book(request,pk):
    try:
        book_instance = Book.objects.get(pk=pk)
        book_instance.is_deleted = True
        book_instance.updater = request.user
        book_instance.save()

        status_code = status.HTTP_200_OK
        response_data = {
            "status": status_code,
            "message": "Successfully Deleted.",
        }
    except Book.DoesNotExist:
        status_code = status.HTTP_404_NOT_FOUND
        response_data = {
            "status": status_code,
            "message": "Not found.",
        }
    return Response(response_data, status=status_code)

# reviews
@api_view(['GET'])
@permission_classes((AllowAny,))
@renderer_classes((JSONRenderer,))
def reviews_list(request):
    
    try :
        instances = Review.objects.filter(is_deleted=False)
        
        serialized = BookReviewSerializer(instances, many=True, context={"request": request})
        average_rating = instances.aggregate(avg_rating=Avg('rating'))['avg_rating']
        
        status_code = status.HTTP_200_OK  
        response_data = {
            "status": status_code,
            "data": serialized.data,
            "average_rating": average_rating,
        }
    except :
        status_code = status.HTTP_400_BAD_REQUEST 
        response_data = {
            "status": status_code,
        }

    return Response(response_data, status_code)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
@renderer_classes((JSONRenderer,))
def create_reviews(request):
    serialized = BookReviewSerializer(data=request.data)
    
    if serialized.is_valid():
        serialized.save(
         auto_id = get_auto_id(Review),
         creator = request.user,
        )
        
        status_code = status.HTTP_200_OK
        response_data = {
            "status": status_code,
            "data": serialized.data,
            "message": "Successfully created"
        }
    else:
        status_code = status.HTTP_400_BAD_REQUEST
        errors = generate_serializer_errors(serialized.errors)
        
        response_data = {
            "status": status_code,
            "message": errors,
        }

    return Response(response_data, status=status_code)


@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
@renderer_classes((JSONRenderer,))
def update_reviews(request,pk):
    try:
        book_instance = Review.objects.get(pk=pk)

        serializer = BookReviewSerializer(book_instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            
            status_code = status.HTTP_200_OK
            response_data = {
                "status": status_code,
                "data": serializer.data,
                "message": "Updated successfully.",
            }
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            response_data = {
                "status": status_code,
                "errors": serializer.errors,
            }
    except Review.DoesNotExist:
        status_code = status.HTTP_404_NOT_FOUND
        response_data = {
            "status": status_code,
            "message": "Not found.",
        }
    return Response(response_data, status=status_code)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
@renderer_classes((JSONRenderer,))
def delete_reviews(request,pk):
    try:
        book_instance = Review.objects.get(pk=pk)
        book_instance.is_deleted = True
        book_instance.updater = request.user
        book_instance.save()

        status_code = status.HTTP_200_OK
        response_data = {
            "status": status_code,
            "message": "Successfully Deleted.",
        }
    except Review.DoesNotExist:
        status_code = status.HTTP_404_NOT_FOUND
        response_data = {
            "status": status_code,
            "message": "Not found.",
        }
    return Response(response_data, status=status_code)