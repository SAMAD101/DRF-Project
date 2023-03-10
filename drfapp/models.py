from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=64)
    age = models.IntegerField()
    description = models.TextField()
    date_enrolled = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'Name: {self.name} \t Age: {self.age}'