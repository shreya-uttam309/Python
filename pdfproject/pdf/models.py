from django.db import models

# Create your models here.
class StudentForm(models.Model):  
   
    file      = models.FileField() # for creating file input  
   
    class Meta:  
        db_table = "pdfs"