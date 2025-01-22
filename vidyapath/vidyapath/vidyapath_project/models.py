from django.db import models

# Create your models here.

class Registration(models.Model):
    name = models.CharField(max_length=100)
    batch = models.CharField(max_length=50)
    rollNo = models.CharField(max_length=20, unique=True)
    smartCardId = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Notice(models.Model):
    description = models.TextField()  # Stores the notice content
    #created_at = models.DateTimeField(auto_now_add=True)  # Stores the time & date when the notice is created

    def __str__(self):
       # return f"Notice {self.id} - {self.created_at.strftime('%d-%m-%Y %H:%M')}"
       return self.description