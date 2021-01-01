from rest_framework import serializers
from PersonApp.models import Person

class personSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ("url", "name", "age")