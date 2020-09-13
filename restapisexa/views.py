from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from restapisexa.models import Book, Author
from rest_framework import routers, viewsets
from restapisexa.serializers import BookSerializer, AuthorSerializer

# Create your views here.


# @api_view(['GET'])
# @csrf_exempt
# @permission_classes([IsAuthenticated])
# def Welcome(request):
#     content = Book.objects.all()
#     return JsonResponse(content)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # permission_classes = [IsAuthenticated]


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
