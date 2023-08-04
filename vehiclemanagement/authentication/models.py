from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustUser(AbstractUser):
    options=(
        ("super_admin","super_admin"),
        ("management_admin","management_admin")
    )
    user_type=models.CharField(max_length=20,choices=options,default='super_admin')