from rest_framework import serializers
from .models import Student,Intrest




class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model =Student
        fields="__all__"

class IntrestSerializer(serializers.ModelSerializer):
    class Meta:
        model =Intrest
        fields="__all__"