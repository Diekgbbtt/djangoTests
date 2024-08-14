from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.http import HttpResponse, JsonResponse


from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer

from db_list.serializers import dataSerializer
from db_list.models import dbGeneral, Database, testTable


from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import renderers




# Create your views here.


class DBListView(APIView):
	
        def get(self, pk, request):
            dbs = Database.objects.all()
            """
            rendering template con dati nell'oggetto db (model)
            """

class testJsonView(APIView):
        

    renderer_classes = [renderers.JSONRenderer]

    def get(request, id):
    
        """
        controllo permessi  https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/ */

        try:
            db = models.Database.objects.get(pk=id)
        except Database.DoesNotExist:
            return HttpResponse(status=404)
        
        dbData = dbGeneral.get_db_data(db.ip, db.port, db.sid, db.tech, db.usr, db.pwd)
        # metodo che chiama anche get_table_columns
        # dbData potrebbe essere una lista di oggetti del modello dbGeneral, in quanto mi aspetto che
        get_db_data faccia una cosa simile a dbGeneral.objects.filter(filters...) oppure dbGeneral.objects.all()
        che richiede di adattare il metodo get_tables_columns a questi metodi dei models in django.
        """
        
        dbData = {} 

        jsonData = get_context_data()

        serializer = dataSerializer(jsonData)

        """"
        The renderers used by the Response class cannot natively handle complex datatypes such as Django model instances, 
        so you need to serialize the data into primitive datatypes before creating the Response object.
        """
        
        return Response(data=serializer.data) # passare template(capire come contesto viene associato ad elementi nel template)

        """
        dbGeneral è un model con attributi ip, port, sid, tech, legal_entity, schema, location ,... 
            e soprattutto tables con lista delle tabelle, ciascuna tabella ha lista delle colonne 
            e ciascuna colonna dettagli tecnici.
        """
    

            #template rendering


def get_context_data():

    context = list()
    rows = testTable.objects.all()

    for row in rows:

        anag = dict()
        anag['name'] = row.name
        anag['surname'] = row.surname
        anag['city'] = row.city
        anag['bday'] = row.bday
        anag['is_married'] = row.is_married
        anag['age'] =  row.age
        context.append(anag)

    return context

class testHTMLrenderContextView(APIView):
    


        renderer_classes = [renderers.TemplateHTMLRenderer]
        """
        Opzionalmente è possible usare StaticHTMLRender
        which expects the response to contain a string of the pre-rendered HTML content.
        """
        
        
        def get(self, request):

            context=get_context_data()
            """
            The TemplateHTMLRenderer will create a RequestContext, 
            using the response.data as the context dict, 
            and determine a template name to use to render the context.
            """
            responseData = {'employees': context}
            return Response(data=responseData, template_name='rendererTest.html')
            # { 'db_id' : self.db }
            # db = self.get.objects.all()