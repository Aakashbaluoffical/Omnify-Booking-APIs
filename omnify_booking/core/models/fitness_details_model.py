from django.db import models





class FitnessClasses(models.Model):

    name = models.CharField(max_length=250)
    dateandtime = models.DateTimeField()
    instructor = models.CharField(max_length=100)
    available_slots = models.IntegerField(null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    class Meta:
        db_table = 'fitness_classes_tbl'
        ordering = ['-created_at']




    def __str__(self):
        return self.name
