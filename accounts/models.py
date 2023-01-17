from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)

    # The Extra Fields For Users
    avatar = models.ImageField(upload_to= "user/%Y/%m/%d", null= True, blank= True)
    phone_number = models.CharField(max_length=50, null= True, blank= True)
    bio = models.TextField(null= True, blank= True)
    student_college = models.CharField(max_length= 100, null= True, blank= True)

    def __str__(self):
        return self.user.username





