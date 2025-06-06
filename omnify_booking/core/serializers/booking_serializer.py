from rest_framework.serializers import ModelSerializer
from core.models.booking_model import Booking
from rest_framework import serializers


class BookingSerializer(ModelSerializer):
    # These are response-only fields (read-only)
    name = serializers.CharField(source='fitness.name', read_only=True)
    dateandtime = serializers.DateTimeField(source='fitness.dateandtime', read_only=True)
    instructor = serializers.CharField(source='fitness.instructor', read_only=True)

    class Meta:
        model = Booking
        fields = [
            'name',          # response only
            'dateandtime',   # response only
            'instructor',     # response only
            'status',        # write + read
            'is_active',     # optional read
            'user',          # write only
            'fitness'       # write only
        ]
         
        extra_kwargs = {
            'user': {'write_only': True},
            'fitness': {'write_only': True},
            'is_active': {'read_only': True}
        }
    def validate(self, attrs):

        user = attrs.get('user')
        fitness = attrs.get('fitness')
        status = attrs.get('status')

        if Booking.objects.filter(user=user, fitness=fitness, status=status, is_active=True).exists():
            raise serializers.ValidationError({"Duplicate Entry": "This booking already exists for the user with the same status."})
        
        return attrs

        
   
    