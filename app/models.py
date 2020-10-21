from django.db import models

# Create your models here.

class Some(models.Model):
    name = models.TextField(max_length=10)
    love = models.TextField()