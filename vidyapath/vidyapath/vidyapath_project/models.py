from django.db import models
from datetime import datetime
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    batch = models.CharField(max_length=100)  # Add a default value
    created_at=models.DateTimeField(default=datetime.now,blank=True)
    #created_at = models.DateTimeField(auto_now_add=True)  # Stores the time & date when the notice is created

    def __str__(self):
       # return f"Notice {self.id} - {self.created_at.strftime('%d-%m-%Y %H:%M')}"
        return f"Notice for Batch {self.batch}"
   

# Signal to send email when a new notice is created
#@receiver(post_save, sender=Notice)
#def send_notice_email(sender, instance, created, **kwargs):
 #   if created:  # Only send an email when a new notice is added
   #     subject = "New Notice Published"
    #    message = f"Dear Student,\n\nA new notice has been published:\n\n{instance.description}\n\nPlease check the website for more details."
     #   sender_email = 'shreyauttam97@gmail.com'  # Same as EMAIL_HOST_USER
      #  recipient_list = Registration.objects.values_list('email', flat=True)  # Get all student emails

        # Send email
       # send_mail(subject, message, sender_email, recipient_list)