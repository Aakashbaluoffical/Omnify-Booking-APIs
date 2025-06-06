from django.db import models
from .user_model import User
from .fitness_details_model import FitnessClasses



class Booking(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    fitness = models.ForeignKey(FitnessClasses,on_delete=models.CASCADE)
    status = models.CharField(max_length=50,choices=[('booked','Booked'),('canceled','Canceled'),('completed','Completed')])
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'booking_tbl'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields= ['status','is_active'])
        ]



    def __str__(self):
        return self.status
