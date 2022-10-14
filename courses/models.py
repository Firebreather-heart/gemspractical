from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
# Create your models here.

class Completionmanager(models.Manager):
    def get_queryset(self):
        return super(Completionmanager, self).get_queryset().filter(status='ongoing')

class Subject(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    student = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='student', on_delete=models.CASCADE)
    started = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=[('FIN', 'completed'), ('ON', 'ongoing')], default='ongoing')
    ongoing = Completionmanager()
    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title 
    
    # def get_absolute_url(self):
    #     return self.

class Task(models.Model):
    name = models.CharField(max_length=1000, db_index=True)
    subject = models.ForeignKey(Subject, related_name='subject', on_delete=models.CASCADE)
    solution = models.TextField(max_length=2500, blank=True)
    deadline = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name 

class Score(models.Model):
    value = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)], blank=True)
    task = models.OneToOneField(Task, related_name='task_score', on_delete=models.CASCADE)