from rest_framework import serializers

from db_list.models import dbGeneral


class dataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = dbGeneral
        fields = ['test_1', 'test_2', 'test_3']

    """
    ModelSerializer :
    The default implementation also does not handle nested relationships.
     If you want to support writable nested relationships you'll need
    to write an explicit `.create()` method.
    """