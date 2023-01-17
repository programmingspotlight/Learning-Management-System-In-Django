from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    is_instructor = models.BooleanField(default= False)
    is_student = models.BooleanField(default= False)

    # The Extra Fields For Users.
    avatar = models.ImageField(upload_to= "user/%Y/%m/%d", null= True, blank= True)
    phone_number = models.CharField(max_length=50, null= True, blank= True)
    bio = models.TextField(null= True, blank= True)

    REQUIRED_FIELDS = ['email',]


