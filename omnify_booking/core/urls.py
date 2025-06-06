
from django.urls import path
from .views import ViewAllClassView ,BookFitnessClass , CreateUser , CreateFitness, LoginView



urlpatterns = [
    path('classes',ViewAllClassView.as_view(),name="upcoming classes"),
    path('book',BookFitnessClass.as_view(),name="Booking classes"),
    path('bookings/<int:pk>',BookFitnessClass.as_view(),name="View all bookings"),


    path('login',LoginView.as_view(),name="login_user"),


    # THis is only for creating user and fitness classes
    path('user/create',CreateUser.as_view(),name="create-user"),
    path('fitness/create',CreateFitness.as_view(),name="create-fitness"),


]
