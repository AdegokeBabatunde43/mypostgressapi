from django.shortcuts import render
from rest_framework.response import Response
from pages.serializer import BookSerializer
from rest_framework.decorators import api_view
from pages.models import Book
# import requests

# Create your views here.

@api_view(['POST'])
def createtodo(request):
    record = BookSerializer(data=request.data)
    if record.is_valid():
        record.save()
    return Response(record.data)

@api_view(['GET'])
def alltodo(request):
    record= Book.objects.all()
    info = BookSerializer(record, many=True)
    return Response(info.data)

@api_view(['DELETE'])
def deletetodo(request,id):
    record=Book.objects.get(id=id)
    record.delete()
    return Response('Products deleted successfully')

@api_view(['GET'])
def detailtodo(request,id):
    record = Book.objects.get(id=id)
    info = BookSerializer(record, many=False)
    return Response(info.data)

@api_view(['PUT'])
def edittodo(request,id):
    record = Book.objects.get(id=id)
    info = BookSerializer(data=request.data, instance=record)
    if info.is_valid():
        info.save()
        return Response('update was successfull')
    
    
# def index(request):
#     url=requests.get('http//localhost:8000/api/v1/alltodo')
#     data=url.json()
#     context={'data': data}
#     return render(request, 'index.html', context)


