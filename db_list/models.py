from django.db import models

from enum import Enum

# Create your models here.


class Database(models.Model):

    def get():
            return None

class dbGeneral(models.Model):
        
            test_1 = models.JSONField()
            test_2 = models.IntegerField()
            test_3 = models.IntegerField()

            """

            def get_db_data():

            def get_tables_columns():
            
            
            """

class GenderEnum(Enum):
    MALE = 'M'
    FEMALE = 'F'


class testTable(models.Model):
    
    name = models.TextField()
    surname = models.TextField()
    city = models.TextField()
    is_married = models.BooleanField()
    bday = models.DateField()
    age = models.IntegerField()




