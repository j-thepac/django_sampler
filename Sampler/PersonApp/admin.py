from django.contrib import admin

# Register your models here.

from .models import Person
from django.contrib import admin

admin.site.register(Person)