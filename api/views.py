# from functools import partial
# import json
# import io

# from re import I, S, T
# import re

#import requests
#from requests.api import request
# from requests.models import Response

import re
from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.views import View
# from django.utils.decorators import method_decorator

# from rest_framework import serializers
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Student
from .serializers import StudentSerializers
#from drf_1.api import serializers


# Create your views here.
#----FBV----#
#---model object for single student data---#
# def student_detail(request, pk):
#     stu = Student.objects.get(id = pk)
#     serializer = StudentSerializers(stu)
#     json_data = JSONRenderer().render(serializer.data)
#     return HttpResponse(json_data, content_type = 'application/json')
    # return JsonResponse(serializer.data)

#---queryset all---#
# def student_list(request):
#     stu = Student.objects.all()
#     serializer = StudentSerializers(stu, many=True)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type = 'application/json')
    # return JsonResponse(serializer.data, safe = False) #does same operation as commented line above in this functionview

#---Function based CRUD view---#
# @csrf_exempt
# def student_create(request):
#     if request.method == 'POST':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         py_data = JSONParser().parse(stream)
#         serializer = StudentSerializers(data = py_data)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':'new student created'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type = 'application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')

# def student_read(request):
#     if request.method == 'GET':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         py_data = JSONParser().parse(stream)
#         id = py_data.get('id',None)
#         if id is not None:
#             stu = Student.objects.get(id = id)
#             serializer = StudentSerializers(stu)
#             json_data = JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data, content_type='application/json')
#         stu = Student.objects.all()
#         serializer = StudentSerializers(stu, many = True)
#         json_data = JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data, content_type='application/json')

# @csrf_exempt
# def student_update(request):
#     if request.method == 'PUT':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         py_data = JSONParser().parse(stream)
#         id =  py_data.get('id')
#         stu = Student.objects.get(id = id)
#         serializer = StudentSerializers(stu, data= py_data, partial = True)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':'Data Updated'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')

# @csrf_exempt
# def student_delete(request):
#     if request.method == 'DELETE':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         py_data = JSONParser().parse(stream)
#         id = py_data.get('id')
#         stu = Student.objects.get(id = id)
#         stu.delete()
#         res = {'msg':'Data Deleted'}
#         json_data = JSONRenderer().render(res)
#         return HttpResponse(json_data, content_type='application/json')

#----CBV CRUD----# 
# @method_decorator(csrf_exempt, name='dispatch')
# class StudentApi(View):
    
#     def get(self, request, *args, **kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         py_data = JSONParser().parse(stream)
#         id = py_data.get('id',None)
#         if id is not None:
#             stu = Student.objects.get(id = id)
#             serializer = StudentSerializers(stu)
#             json_data = JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data, content_type='application/json')
#         stu = Student.objects.all()
#         serializer = StudentSerializers(stu, many = True)
#         json_data = JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data, content_type='application/json')

#     def post(self, request, *args, **kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         py_data = JSONParser().parse(stream)
#         serializer = StudentSerializers(data = py_data)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':'new student created'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type = 'application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')

#     def put(self, request, *args, **kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         py_data = JSONParser().parse(stream)
#         id =  py_data.get('id')
#         stu = Student.objects.get(id = id)
#         serializer = StudentSerializers(stu, data= py_data, partial = True) #partial true = patch
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':'Data Updated'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')

#     def delete(self, request, *args, **kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         py_data = JSONParser().parse(stream)
#         id = py_data.get('id')
#         stu = Student.objects.get(id = id)
#         stu.delete()
#         res = {'msg':'Data Deleted'}
#         json_data = JSONRenderer().render(res)
#         return HttpResponse(json_data, content_type='application/json')

#----Function Based API view----#
# @api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
# def student_api(request, pk = None):
    
#     if request.method == 'GET':
#         id = pk
#         if id is not None:
#             stu = Student.objects.get(id = id)
#             serializer = StudentSerializers(stu)
#             return Response(serializer.data)
#         stu = Student.objects.all()
#         serializer = StudentSerializers(stu, many= True)
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = StudentSerializers(data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Data Created'}, status= status.HTTP_201_CREATED)
#         return Response(serializer.errors)
    
#     if request.method == 'PUT':
#         id = pk
#         stu = Student.objects.get(pk = id)
#         serializer = StudentSerializers(stu, data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Complete Data Updated'})
#         return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
#     if request.method == 'PATCH':
#         id = pk
#         stu = Student.objects.get(pk = id)
#         serializer = StudentSerializers(stu, data= request.data, partial = True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Partial Data Updated'})
#         return Response(serializer.errors)
    
#     if request.method == 'DELETE':
#         id =pk
#         stu = Student.objects.get(pk = id)
#         stu.delete()
#         return Response({'msg': 'Data Deleted'})

#Class Based API View
class StudentAPI(APIView):
    def get(self, request, pk= None, format= None):
        id= pk
        if id is not None:
            stu = Student.objects.get(id = id)
            serializer = StudentSerializers(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializers(stu, many= True)
        return Response(serializer.data)
    
    def post(self, request, format= None):
        serializer = StudentSerializers(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status= status.HTTP_201_CREATED)
        return Response(serializer.errors)
    
    def put(self, request, pk= None, format= None):
        id = pk
        stu = Student.objects.get(pk = id)
        serializer = StudentSerializers(stu, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Updated'})
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk= None, format= None):
        id = pk
        stu = Student.objects.get(pk = id)
        serializer = StudentSerializers(stu, data= request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated'})
        return Response(serializer.errors)
    
    def delete(self, request, pk= None, format= None):
        id =pk
        stu = Student.objects.get(pk = id)
        stu.delete()
        return Response({'msg': 'Data Deleted'})