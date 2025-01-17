from django.db import models

# Create your models here.
from django.db import models
class User(models.Model):
    uname = models.CharField(max_length=100)  # Stores the user's name
    ubatch = models.CharField(max_length=20)  # Stores the user's batch
    uroll_no = models.CharField(max_length=50, unique=True)  # Unique roll number
    uid = models.CharField(max_length=50, unique=True)  # Unique Smart Card ID
    email = models.EmailField(unique=True)  # Email must be unique
    upass = models.CharField(max_length=128)  # User's password
    
    class Meta:
        db_table="user"

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    roll_number = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Notice(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title