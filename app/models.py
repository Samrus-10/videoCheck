from django.db import models

# Create your models here.

class Some(models.Model):
    name = models.ChartField(max_length=10)
