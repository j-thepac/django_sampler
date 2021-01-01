# Django Step by Step

**Pre- Req:**
1. python 3+
2. pip install virtualenv
3. source ~/project/bin/activate

##Basic Installation
    

    $pip install django
    $pip install djangorestframework
    $django-admin startproject Main
    $python manage.py runserver

    
open http://127.0.0.1:8000/

##Create a Person App

    $python manage.py startapp PersonApp
     
- create a folder "templates" in project

- create a folder "static" in project
     
- Under settings.py 
    
    
    import os
    INSTALLED_APPS add "PersonApp"
    STATIC_URL ='/static/'
    STATICFILES_DIR=[os.path.join(BASE_DIR,'static'),'/var/www/static/']
    TEMPLATES= ['DIRS': [os.path.join(BASE_DIR,'templates')]
     
Under urls.py
 
    from django.urls import path,include
    path('', include('PersonApp.urls'))

 

Under PersonApp/views.py


     from django.shortcuts import render 
    def person(request):return render(request,'person.html',{"key":"value"})

Under PersonApp/urls.py


     from django.urls import path 
    from . import views
    urlpatterns= [path('',views.person,name='person')]
     
**Inside folder templates**


- create base_template.html 

- copy paste starter template bootstrap from google

- replace the contents of  body tag with template parameters


    {% block body %} {% endblock body %}

- create person.html


    {% extends 'base_template.html' %}
    {% block body %} Deepak {% endblock body %} 
     

Under PersonApp/models.py (Create Model (DB)) 

    from django.db import models

    class Person(models.Model):
        id=models.AutoField(primary_key=True)
        name=models.CharField(max_length=64)
        age=models.IntegerField(default=0)

UnderPersonApp/admin.py 

    from .models import Person
    from django.contrib import admin
    admin.site.register(Person)

Migrate to Create DB
     
    python manage.py makemigrations 
    python manage.py migrate
     python manage.py createsuperuser
    Add new person to DB

open http://127.0.0.1:8000/admin

Verify the tables created



## To display the Person in html 

   Edit PersonApp/views.py

    from django.shortcuts import render
    from .models import Person
    def person(request):return render(request,'person.html',{"person":Person.objects.all()})

   Edit person.html

    {% extends 'base_template.html' %}
    {% block body %} Deepak

    <div>
        {% for i in person %}
        <tr>
            <td> {{ i.name }}</td>
            <td> {{ i.age }}</td>
        </tr>
        {%endfor%}
    </div>

    {% endblock body %}

open http://127.0.0.1:8000/


     
## Add API 

     

    pip install djangorestframework
    pip freeze > requirements.txt
    python manage.py startapp api
    
- settings.py > INSTALLED_APPS = 'rest_framework' ,'api'
   
- url.py > urlpatterns=[path('api/', include('api.urls')),]

- create  api/serializers.py : Converts models to Json 


    from rest_framework import serializers
    from  PersonApp.models import Person

    class personSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Person
            fields = ("url","name","last_name")

api/views.py
    
    from rest_framework import viewsets
    from PersonApp.models import Person
    from .serializers import personSerializer

    #make sure Person model is created in models.py and migrated
    class personView(viewsets.ModelViewSet):
        queryset = Person.objects.all()
        serializer_class = personSerializer

create  api/urls.py : Handles all API endpoint

        from django.urls import path , include
        from . import views
        from rest_framework import routers

        router = routers.DefaultRouter() 
        router.register('person',views.personview)
        urlpatterns = [path('', include(router.urls))]

 
open http://127.0.0.1:8000/api


 