from django.db import models

# Create your models here.
class PlacementStatistic(models.Model):
    year = models.IntegerField()
    company_name = models.CharField(max_length=255)
    students_placed = models.IntegerField()
    average_package = models.FloatField()
    highest_package = models.FloatField()
    role_offered = models.CharField(max_length=255)
    recruitment_type = models.CharField(max_length=50, choices=[('On-campus', 'On-campus'), ('Off-campus', 'Off-campus')])

  
    def __str__(self):
        return f"{self.company_name} ({self.year})"