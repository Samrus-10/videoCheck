from django.db import models

# Create your models here.

class Some(models.Model):
    
    name = models.TextField(max_length=10)
    love = models.TextField()
    
class FILE(models.Model):
    
    file_name = models.FileField(upload_to="static/file/", validators=[validate_file_extension])
    directions = models.TextField()
