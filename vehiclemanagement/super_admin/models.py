from django.db import models

# Create your models here.


class Vehicle(models.Model):
    vehicle_number = models.CharField(max_length=100,null=True)
    vehicle =(
        ("Two Wheeler","Two Wheeler"),
        ("Three Wheeler","Three Wheeler"),
        ("Four Wheeler","Four Wheeler"),
        
    )
    vehicle_type = models.CharField(max_length=50,choices=vehicle, default="Two Wheeler")
    vehicle_model = models.CharField(max_length=50)
    vehicle_description = models.CharField(max_length=100,null=True)

    # def save(self, *args, **kwargs):
    #     self.vehicle_number = self.vehicle_number.upper()
    #     self.vehicle_model = self.vehicle_type.upper()
    #     super().save(*args, **kwargs) 
    
    def __str__(self):
        return self.vehicle_number