from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from doerscontact.models import Contact
from doerscontact.serializers import ContactSerializer
from rest_framework.response import Response

@csrf_exempt
def contact_list(request):
    """
    List all contact list, or create a a new contact.
    """
    if request.method == 'GET':
        c = Contact.objects.all()
        serializer = ContactSerializer(c, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ContactSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def contact_detail(request, pk):
    try:
        c = Contact.objects.get(pk=pk)
    
    except Contact.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = ContactSerializer(c)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)        
        serializer = ContactSerializer(c, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        c.delete()
        return HttpResponse(status=204)
        

