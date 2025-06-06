from .serializers.booking_serializer import BookingSerializer
from .serializers.fitness_details_serializer import FitnessSerializer

from .models.fitness_details_model import FitnessClasses
from .models.user_model import User
from .models.booking_model import Booking


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from datetime import datetime
from django.contrib.auth import authenticate



# Create your views here.

class ViewAllClassView(APIView):
    #==================================================
    #  To View all upcoming classes
    #====================================================
    def get(self, request):
        today = datetime.now()
        fitness_classes = FitnessClasses.objects.filter(
            is_active=True,
            dateandtime__gt=today,
            available_slots__gt = 0)
        serializer = FitnessSerializer(fitness_classes,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)



class BookFitnessClass(APIView):
    #==================================================
    #  To booking slots
    #==================================================== 
    def post(self,request):
        print(request.data['user_id'],"=======================================")
        user = User.objects.filter(pk = request.data['user_id'],is_active=True).first()
        fitness = FitnessClasses.objects.filter(pk = request.data['class_id'],is_active=True).first()
        if not fitness:
            return Response(serializer.errors, status=400)
        print(fitness.available_slots,"==++++++=====================================")
        if fitness.available_slots <= 0:
            return Response({"Status:Booking Full"}, status=200) 


        print(user,"=======================================")
        print(fitness,"  fitness=======================================")

        data = {    "user":user.id,
                    "fitness":fitness.id,
                    "status": "booked"
                }
        

        serializer = BookingSerializer(data=data)
        if serializer.is_valid():
            serializer.save(is_active=True) 
            # return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)

        fitness.available_slots-=1
        fitness.save()
        return Response(serializer.data, status=201)


    #==================================================
    #  To get all booked slots
    #====================================================     
    def get(self,request,pk):

        user = get_object_or_404(User, pk= pk,is_active=True)
        print(user,"============================")
        bookings = Booking.objects.filter(is_active=True,user = user)
        serializer = BookingSerializer(bookings, many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)





#==================================================
#  To create Users and add classes
#==================================================== 
from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'name', 'email', 'role', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user

class CreateUser(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class CreateFitness(APIView):
    def post(self, request):
        serializer = FitnessSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(is_active=True)  # Force active
            return Response({"message": "Fitness class created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class LoginView(APIView):
   
   

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            return Response({
                "message": "Login successful",
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "name": user.name,
                    
        
                }
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)