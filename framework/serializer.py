# serializers.py
from rest_framework import serializers
from .models import *

class AdvocateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advocate
        fields = '__all__'

class SupremeSerializer(serializers.ModelSerializer):
    advocate = AdvocateSerializer()
    # employee_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Supreme
        fields = '__all__'
    
    # def get_employee_count(self, obj):
    #     count = obj.advocate_set.count()
    #     return count
