from django.db import models
from .validators import validate_file_extension

# Create your models here.
    
class FILE(models.Model):
    
    file_name = models.FileField(upload_to="static/file/", validators=[validate_file_extension])
    directions = models.TextField()
    file_clear_name = models.TextField()




class DataMarket(models.Model):
    
    id_station = models.TextField()
    #mark =  models.TextField()
    year = models.TextField()
    month = models.TextField()
    day = models.TextField()
    hours = models.TextField()
    minutes = models.TextField()
    seconds = models.TextField()
    
