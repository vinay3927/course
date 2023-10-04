from rest_framework import serializers
from .models import Course
from .models import CourseDelivery

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__' 
        
class CourseDeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseDelivery
        fields = '__all__'
