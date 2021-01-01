from django.shortcuts import render
from rest_framework import viewsets
from .serializers import personSerializer
from PersonApp.models import Person


class personView(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = personSerializer
