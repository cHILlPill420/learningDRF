from functools import partial
import json
from re import I, S, T
import re
from django.shortcuts import render
import requests
from requests.api import request
from rest_framework import serializers
from .models import Student
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.utils.decorators import method_decorator

# Create your views here.

#model object for single student data
def student_detail(request, pk):
    stu = Student.objects.get(id = pk)
    serializer = StudentSerializers(stu)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type = 'application/json')
    # return JsonResponse(serializer.data)

#queryset all
def student_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializers(stu, many=True)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type = 'application/json')
    return JsonResponse(serializer.data, safe = False) #does same operation as commented line above in this functionview

#CRUD student
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

#CBV CRUD 
@method_decorator(csrf_exempt, name='dispatch')
class StudentApi(View):
    
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream)
        id = py_data.get('id',None)
        if id is not None:
            stu = Student.objects.get(id = id)
            serializer = StudentSerializers(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        stu = Student.objects.all()
        serializer = StudentSerializers(stu, many = True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream)
        serializer = StudentSerializers(data = py_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'new student created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type = 'application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream)
        id =  py_data.get('id')
        stu = Student.objects.get(id = id)
        serializer = StudentSerializers(stu, data= py_data, partial = True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream)
        id = py_data.get('id')
        stu = Student.objects.get(id = id)
        stu.delete()
        res = {'msg':'Data Deleted'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')
