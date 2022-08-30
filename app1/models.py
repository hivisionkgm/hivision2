from django.db import models

class feedbackmodel(models.Model):
    name=models.CharField(max_length=40)
    email=models.CharField(max_length=40)
    message=models.CharField(max_length=200)


# Create your models here.
