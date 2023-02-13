from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings 
from datetime import datetime
import uuid 
from django.urls import reverse
# Create your models here.

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    CLASS_CHOICES = (('J1','JSS 1'), ('J2','JSS 2'), ('J3', 'JSS 3'), ('S1','SS 1'), ('S2','SS 2'), ('S3', 'SS 3'))
    date_of_birth = models.DateField(blank=True, null=True)
    cls = models.CharField(max_length=10, choices = CLASS_CHOICES)
    GENDER_CLASSES = (('ML','male'),('FM','female'),('N','neuter'))
    gender = models.CharField(max_length=10, choices=GENDER_CLASSES, default='N')
    department = models.CharField(max_length=120, choices=(('ARTS','arts'),('COMM','commercial'), ('SCI','science')), blank=True, null=True)

    def __str__(self):
        return self.first_name
    

class Profile(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    CLASS_CHOICES = (('J1','JSS 1'), ('J2','JSS 2'), ('J3', 'JSS 3'), ('S1','SS 1'), ('S2','SS 2'), ('S3', 'SS 3'))
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    first_name = models.CharField(max_length=30, default='')
    last_name = models.CharField(max_length=30, default='')
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%M/%D/', blank=True, null=True)
    cls = models.CharField(max_length=10, choices = CLASS_CHOICES)
    GENDER_CLASSES = (('ML','male'),('FM','female'),('N','neuter'))
    gender = models.CharField(max_length=10, choices=GENDER_CLASSES, default='N')
    department = models.CharField(max_length=120, choices=(('ARTS','arts'),('COMM','commercial'), ('SCI','science')), blank=True, null=True)

    def __str__(self):
        return f'Profile for {self.user.first_name} {self.user.last_name}'
    
    def get_age(self):
        init_year = self.date_of_birth.year
        final_year = datetime.now().strftime('%Y')
        final_year = int(final_year)
        age = final_year - init_year
        return age
    
    def get_absolute_url(self):
        return reverse('admin_student_dashboard', args=[self.id])