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
            
            dbData = {'POSITIONAL': [{'COLUMN_NAME': 'VAL1', 'DATA_TYPE': 'VARCHAR', 'LENGTH': 670, 'SCALE': 0, 'DEFAULT': None, 'DESCRIPTION': None, 'NULLS': 'Y', 'IDENTITY': 'N'}, {'COLUMN_NAME': 'VAL2', 'DATA_TYPE': 'VARCHAR', 'LENGTH': 670, 'SCALE': 0, 'DEFAULT': None, 'DESCRIPTION': None, 'NULLS': 'Y', 'IDENTITY': 'N'}], 'PRV': [{'COLUMN_NAME': 'VAL', 'DATA_TYPE': 'CHARACTER', 'LENGTH': 30, 'SCALE': 0, 'DEFAULT': None, 'DESCRIPTION': None, 'NULLS': 'Y', 'IDENTITY': 'N'}], 'PRV2': [{'COLUMN_NAME': 'IDT', 'DATA_TYPE': 'DECIMAL', 'LENGTH': 10, 'SCALE': 0, 'DEFAULT': None, 'DESCRIPTION': None, 'NULLS': 'Y', 'IDENTITY': 'N'}, {'COLUMN_NAME': 'VAL', 'DATA_TYPE': 'CHARACTER', 'LENGTH': 30, 'SCALE': 0, 'DEFAULT': None, 'DESCRIPTION': None, 'NULLS': 'Y', 'IDENTITY': 'N'}], 'TEST': [{'COLUMN_NAME': 'IDX', 'DATA_TYPE': 'INTEGER', 'LENGTH': 4, 'SCALE': 0, 'DEFAULT': None, 'DESCRIPTION': None, 'NULLS': 'Y', 'IDENTITY': 'N'}, {'COLUMN_NAME': 'VALUE1', 'DATA_TYPE': 'VARCHAR', 'LENGTH': 255, 'SCALE': 0, 'DEFAULT': None, 'DESCRIPTION': None, 'NULLS': 'Y', 'IDENTITY': 'N'}], 'TESTTABÃLE': [{'COLUMN_NAME': 'VALUE1', 'DATA_TYPE': 'VARCHAR', 'LENGTH': 255, 'SCALE': 0, 'DEFAULT': None, 'DESCRIPTION': None, 'NULLS': 'Y', 'IDENTITY': 'N'}], 'TEST_PART': [{'COLUMN_NAME': 'MONTH', 'DATA_TYPE': 'INTEGER', 'LENGTH': 4, 'SCALE': 0, 'DEFAULT': None, 'DESCRIPTION': None, 'NULLS': 'Y', 'IDENTITY': 'N'}, {'COLUMN_NAME': 'YEAR', 'DATA_TYPE': 'INTEGER', 'LENGTH': 4, 'SCALE': 0, 'DEFAULT': None, 'DESCRIPTION': None, 'NULLS': 'Y', 'IDENTITY': 'N'}], 'TEST_PART2': [{'COLUMN_NAME': 'CAMPO_VARIABILE', 'DATA_TYPE': 'VARCHAR', 'LENGTH': 19834, 'SCALE': 0, 'DEFAULT': None, 'DESCRIPTION': None, 'NULLS': 'Y', 'IDENTITY': 'N'}, {'COLUMN_NAME': 'CAT_MOVI', 'DATA_TYPE': 'DECIMAL', 'LENGTH': 1, 'SCALE': 0, 'DEFAULT': None, 'DESCRIPTION': None, 'NULLS': 'Y', 'IDENTITY': 'N'}, {'COLUMN_NAME': 'CAUSALE_ABI_MOVI', 'DATA_TYPE': 'CHARACTER', 'LENGTH': 2, 'SCALE': 0, 'DEFAULT': None, 'DESCRIPTION': None, 'NULLS': 'Y', 'IDENTITY': 'N'}, {'COLUMN_NAME': 'CAUSALE_CONTR_MOVI', 'DATA_TYPE': 'CHARACTER', 'LENGTH': 2, 'SCALE': 0, 'DEFAULT': None, 'DESCRIPTION': None, 'NULLS': 'Y', 'IDENTITY': 'N'}, {'COLUMN_NAME': 'CAUSALE_MOVI', 'DATA_TYPE': 'DECIMAL', 'LENGTH': 3, 'SCALE': 0, 'DEFAULT': None, 'DESCRIPTION': None, 'NULLS': 'Y', 'IDENTITY': 'N'}, {'COLUMN_NAME': 'CODABI_MOVI', 'DATA_TYPE': 'DECIMAL', 'LENGTH': 5, 'SCALE': 0, 'DEFAULT': None, 'DESCRIPTION': None, 'NULLS': 'Y', 'IDENTITY': 'N'}, {'COLUMN_NAME': 'CONTO_MOVI', 'DATA_TYPE': 'DECIMAL', 'LENGTH': 13, 'SCALE': 0, 'DEFAULT': None, 'DESCRIPTION': None, 'NULLS': 'Y', 'IDENTITY': 'N'}, {'COLUMN_NAME': 'COSTO_MOVI', 'DATA_TYPE': 'CHARACTER', 'LENGTH': 1, 'SCALE': 0, 'DEFAULT': None, 'DESCRIPTION': None, 'NULLS': 'Y', 'IDENTITY': 'N'}, {'COLUMN_NAME': 'COSTO_TPCC_MOVI', 'DATA_TYPE': 'CHARACTER', 'LENGTH': 1, 'SCALE': 0, 'DEFAULT': None, 'DESCRIPTION': None, 'NULLS': 'Y', 'IDENTITY': 'N'}, {'COLUMN_NAME': 'CRO_MOVI', 'DATA_TYPE': 'DECIMAL', 'LENGTH': 11, 'SCALE': 0, 'DEFAULT': None, 'DESCRIPTION': None, 'NULLS': 'Y', 'IDENTITY': 'N'}, {'COLUMN_NAME': 'DATA_MOVI', 'DATA_TYPE': 'DECIMAL', 'LENGTH': 9, 'SCALE': 0, 'DEFAULT': None, 'DESCRIPTION': None, 'NULLS': 'Y', 'IDENTITY': 'N'}, {'COLUMN_NAME': 'DIPATT_MOVI', 'DATA_TYPE': 'DECIMAL', 'LENGTH': 5, 'SCALE': 0, 'DEFAULT': None, 'DESCRIPTION': None, 'NULLS': 'Y', 'IDENTITY': 'N'}, {'COLUMN_NAME': 'DIP_MOVI', 'DATA_TYPE': 'DECIMAL', 'LENGTH': 5, 'SCALE': 0, 'DEFAULT': None, 'DESCRIPTION': None, 'NULLS': 'Y', 'IDENTITY': 'N'}, {'COLUMN_NAME': 'DIP_ORIG_MOVI', 'DATA_TYPE': 'DECIMAL', 'LENGTH': 5, 'SCALE': 0, 'DEFAULT': None, 'DESCRIPTION': None, 'NULLS': 'Y', 'IDENTITY': 'N'}, {'COLUMN_NAME': 'DIVISA_MOVI', 'DATA_TYPE': 'CHARACTER', 'LENGTH': 3, 'SCALE': 0, 'DEFAULT': None, 'DESCRIPTION': None, 'NULLS': 'Y', 'IDENTITY': 'N'}, {'COLUMN_NAME': 'DIVORIG_MOVI', 'DATA_TYPE': 'CHARACTER', 'LENGTH': 3, 'SCALE': 0, 'DEFAULT': None, 'DESCRIPTION': None, 'NULLS': 'Y', 'IDENTITY': 'N'}, {'COLUMN_NAME': 'EUROLIRA_MOVI', 'DATA_TYPE': 'DECIMAL', 'LENGTH': 1, 'SCALE': 0, 'DEFAULT': None, 'DESCRIPTION': None, 'NULLS': 'Y', 'IDENTITY': 'N'}, {'COLUMN_NAME': 'FILLER1', 'DATA_TYPE': 'CHARACTER', 'LENGTH': 6, 'SCALE': 0, 'DEFAULT': "' '", 'DESCRIPTION': None, 'NULLS': 'Y', 'IDENTITY': 'N'}, {'COLUMN_NAME': 'FILLER2', 'DATA_TYPE': 'CHARACTER', 'LENGTH': 7, 'SCALE': 0, 'DEFAULT': "' '", 'DESCRIPTION': None, 'NULLS': 'Y', 'IDENTITY': 'N'}, {'COLUMN_NAME': 'FL_INIZ_CONF_MOVI', 'DATA_TYPE': 'CHARACTER', 'LENGTH': 1, 'SCALE': 0, 'DEFAULT': None, 'DESCRIPTION': None, 'NULLS': 'Y', 'IDENTITY': 'N'}, {'COLUMN_NAME': 'FL_RETE_MOVI', 'DATA_TYPE': 'CHARACTER', 'LENGTH': 1, 'SCALE': 0, 'DEFAULT': None, 'DESCRIPTION': None, 'NULLS': 'Y', 'IDENTITY': 'N'}, {'COLUMN_NAME': 'IMPCOSTO_MOVI', 'DATA_TYPE': 'DECIMAL', 'LENGTH': 9, 'SCALE': 3, 'DEFAULT': None, 'DESCRIPTION': None, 'NULLS': 'Y', 'IDENTITY': 'N'}, {'COLUMN_NAME': 'IMPORIG_MOVI', 'DATA_TYPE': 'DECIMAL', 'LENGTH': 17, 'SCALE': 3, 'DEFAULT': None, 'DESCRIPTION': None, 'NULLS': 'Y', 'IDENTITY': 'N'}, {'COLUMN_NAME': 'IMP_MOVI', 'DATA_TYPE': 'DECIMAL', 'LENGTH': 17, 'SCALE': 3, 'DEFAULT': None, 'DESCRIPTION': None, 'NULLS': 'Y', 'IDENTITY': 'N'}, {'COLUMN_NAME': 'NO_PARTITA_MOVI', 'DATA_TYPE': 'DECIMAL', 'LENGTH': 5, 'SCALE': 0, 'DEFAULT': None, 'DESCRIPTION': None, 'NULLS': 'Y', 'IDENTITY': 'N'}, {'COLUMN_NAME': 'N_ASS_MOVI', 'DATA_TYPE': 'CHARACTER', 'LENGTH': 9, 'SCALE': 0, 'DEFAULT': None, 'DESCRIPTION': None, 'NULLS': 'Y', 'IDENTITY': 'N'}, {'COLUMN_NAME': 'N_BADGE_MOVI', 'DATA_TYPE': 'DECIMAL', 'LENGTH': 7, 'SCALE': 0, 'DEFAULT': None, 'DESCRIPTION': None, 'NULLS': 'Y', 'IDENTITY': 'N'}, {'COLUMN_NAME': 'N_MESS_MOVI', 'DATA_TYPE': 'DECIMAL', 'LENGTH': 7, 'SCALE': 0, 'DEFAULT': None, 'DESCRIPTION': None, 'NULLS': 'Y', 'IDENTITY': 'N'}, {'COLUMN_NAME': 'PRIMO_RIF_MOVI', 'DATA_TYPE': 'CHARACTER', 'LENGTH': 16, 'SCALE': 0, 'DEFAULT': None, 'DESCRIPTION': None, 'NULLS': 'Y', 'IDENTITY': 'N'}, {'COLUMN_NAME': 'PROC_ORIG_MOVI', 'DATA_TYPE': 'CHARACTER', 'LENGTH': 2, 'SCALE': 0, 'DEFAULT': None, 'DESCRIPTION': None, 'NULLS': 'Y', 'IDENTITY': 'N'}, {'COLUMN_NAME': 'PROG_MATR_MOVI', 'DATA_TYPE': 'DECIMAL', 'LENGTH': 7, 'SCALE': 0, 'DEFAULT': None, 'DESCRIPTION': None, 'NULLS': 'Y', 'IDENTITY': 'N'}, {'COLUMN_NAME': 'SALCON_MOVI', 'DATA_TYPE': 'DECIMAL', 'LENGTH': 18, 'SCALE': 3, 'DEFAULT': None, 'DESCRIPTION': None, 'NULLS': 'Y', 'IDENTITY': 'N'}, {'COLUMN_NAME': 'SECONDO_RIF_MOVI', 'DATA_TYPE': 'CHARACTER', 'LENGTH': 16, 'SCALE': 0, 'DEFAULT': None, 'DESCRIPTION': None, 'NULLS': 'Y', 'IDENTITY': 'N'}, {'COLUMN_NAME': 'TIPORAPP_MOVI', 'DATA_TYPE': 'DECIMAL', 'LENGTH': 3, 'SCALE': 0, 'DEFAULT': None, 'DESCRIPTION': None, 'NULLS': 'Y', 'IDENTITY': 'N'}, {'COLUMN_NAME': 'TIPO_CONTEGG_MOVI', 'DATA_TYPE': 'CHARACTER', 'LENGTH': 1, 'SCALE': 0, 'DEFAULT': None, 'DESCRIPTION': None, 'NULLS': 'Y', 'IDENTITY': 'N'}, {'COLUMN_NAME': 'VALUTA_MOVI', 'DATA_TYPE': 'DECIMAL', 'LENGTH': 9, 'SCALE': 0, 'DEFAULT': None, 'DESCRIPTION': None, 'NULLS': 'Y', 'IDENTITY': 'N'}], 'TEST_ZCF': [{'COLUMN_NAME': 'FAMILIENNAME', 'DATA_TYPE': 'CHARACTER', 'LENGTH': 32, 'SCALE': 0, 'DEFAULT': None, 'DESCRIPTION': None, 'NULLS': 'N', 'IDENTITY': 'N'}, {'COLUMN_NAME': 'MA_INFOTEXT', 'DATA_TYPE': 'CHARACTER', 'LENGTH': 32, 'SCALE': 0, 'DEFAULT': None, 'DESCRIPTION': None, 'NULLS': 'N', 'IDENTITY': 'N'}, {'COLUMN_NAME': 'MA_INFOTEXT_KURZ', 'DATA_TYPE': 'CHARACTER', 'LENGTH': 32, 'SCALE': 0, 'DEFAULT': None, 'DESCRIPTION': None, 'NULLS': 'N', 'IDENTITY': 'N'}, {'COLUMN_NAME': 'OE_KURZKENNUNG', 'DATA_TYPE': 'CHARACTER', 'LENGTH': 7, 'SCALE': 0, 'DEFAULT': None, 'DESCRIPTION': None, 'NULLS': 'N', 'IDENTITY': 'N'}, {'COLUMN_NAME': 'UNTERNEHM_BEREICH', 'DATA_TYPE': 'CHARACTER', 'LENGTH': 2, 'SCALE': 0, 'DEFAULT': None, 'DESCRIPTION': None, 'NULLS': 'N', 'IDENTITY': 'N'}, {'COLUMN_NAME': 'VORNAME', 'DATA_TYPE': 'CHARACTER', 'LENGTH': 32, 'SCALE': 0, 'DEFAULT': None, 'DESCRIPTION': None, 'NULLS': 'N', 'IDENTITY': 'N'}]}
        

            serializer = dataSerializer(dbData)

            """"
            The renderers used by the Response class cannot natively handle complex datatypes such as Django model instances, 
            so you need to serialize the data into primitive datatypes before creating the Response object.
            """
            
            return Response(data=dbData) # passare template(capire come contesto viene associato ad elementi nel template)

            """
            dbGeneral è un model con attributi ip, port, sid, tech, legal_entity, schema, location ,... 
                e soprattutto tables con lista delle tabelle, ciascuna tabella ha lista delle colonne 
                e ciascuna colonna dettagli tecnici.
            """
    

            #template rendering


class testHTMLrenderContextView(APIView):
    
        def get_context_data(self, **kwargs):
        
            context = dict()
            rows = testTable.objects.all()

            for i in range(1, len(rows)):
                context[i] = dict()
                context[i]['name'] = rows[i].name
                context[i]['surname'] = rows[i].surname
                context[i]['city'] = rows[i].city
                context[i]['bday'] = rows[i].bday
                context[i]['is_married'] = rows[i].is_married
                context[i]['age'] =  rows[i].age

            return context

        renderer_classes = [renderers.TemplateHTMLRenderer]
        """
        Opzionalmente è possible usare StaticHTMLRender
        which expects the response to contain a string of the pre-rendered HTML content.
        """
        
        
        def get(self, request):

            context=self.get_context_data()
            """
            The TemplateHTMLRenderer will create a RequestContext, 
            using the response.data as the context dict, 
            and determine a template name to use to render the context.
            """

            rs = Response(data=context, template_name='rendererTest.html')
            # { 'db_id' : self.db }
            # db = self.get.objects.all()
            return rs