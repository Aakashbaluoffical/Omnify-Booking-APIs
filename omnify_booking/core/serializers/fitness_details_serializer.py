from rest_framework.serializers import ModelSerializer
from core.models.fitness_details_model import FitnessClasses
from rest_framework import serializers




class FitnessSerializer(ModelSerializer):
    class Meta:
        model = FitnessClasses 
        fields = ['id','name','dateandtime','instructor','available_slots','is_active']
        

    def validate(self, attrs):
        if not attrs.get('name'):
            raise serializers.ValidationError({"name": "This field is required."})
        if not attrs.get('dateandtime'):
            raise serializers.ValidationError({"dateandtime": "This field is required."})
        if not attrs.get('instructor'):
            raise serializers.ValidationError({"instructor": "This field is required."})
        if attrs.get('available_slots') is None or attrs.get('available_slots') < 1:
            raise serializers.ValidationError({"available_slots": "Available slots must be a positive integer."})
        
        if FitnessClasses.objects.filter(name=attrs.get('name'),dateandtime = attrs.get('dateandtime'),instructor = attrs.get('instructor')):
             raise serializers.ValidationError({"Duplicate Entry": "name, dateandtime, instructor"})
        return attrs