from django.db import models

# Create your models here.
class employee(models.Model):
    SEX_CHOICES=[('M','Male'),('F','Female')]
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    age=models.IntegerField(null=True)
    # def __str__(self):
    #     return self.name

class role(models.Model):
    role_id = models.CharField(max_length=10) 
    # def __str__(self):
    #     return self.name