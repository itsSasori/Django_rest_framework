from django.http import JsonResponse
from django.shortcuts import render , redirect
from django.db.models import Q
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from .serializer import *
from .models import *
from rest_framework.permissions import IsAuthenticated


# Create your views here.

@api_view(['GET'])
def home(request):
    data  = ['advocate']
    return Response(data)


@api_view(['GET','POST'])
def create_advocate(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query == None:
              query=''

        advocate = Advocate.objects.filter(Q(username__icontains=query) | Q(bio__icontains=query))      
        serializer = AdvocateSerializer(advocate, many=True)
        return Response(serializer.data)
    
    if request.method=='POST':
        
        advocate = Advocate.objects.create(
                username = request.data['username'],
                bio  = request.data['bio']
            )

        serializer = AdvocateSerializer(advocate,many=False)
        return Response(serializer.data)
    
@api_view(['GET','PUT','DELETE'])
def list_advocate(request,username):
    advocate = Advocate.objects.get(username=username)
    if request.method == "GET":
                serializer = AdvocateSerializer(advocate,many=False)
                return Response(serializer.data)
    
    if request.method == "PUT":
                advocate.username = request.data['username']
                advocate.bio = request.data['bio']
                advocate.save()
                serializer = AdvocateSerializer(advocate, many=False)
                return Response(serializer.data)
    
    if request.method == "DELETE":
          advocate.delete()
          return redirect('/')
    

@api_view(['GET','POST'])
def list_supreme(request):
    if request.method == 'GET':
        supreme = Supreme.objects.all()      
        serializer = SupremeSerializer(supreme, many=True)
        return Response(serializer.data)
    
            
            
                






