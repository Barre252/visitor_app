from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


# User Model 'Extended'
class CustomUser(AbstractUser):
    tell = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
         return self.username
    
class VisitorRegistration(models.Model):

    VISIT_STATUS = (
        ('Waiting', 'Waiting'),
        ('Next', 'Next'),
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed'),
        ('Postponed', 'Postponed'),
        ('Cancelled', 'Cancelled'),
        ('Rejected', 'Rejected')
    )

    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    person_to_visit = models.CharField(max_length=30)
    visit_reason = models.TextField()
    hours_to_stay = models.IntegerField(null=True, blank=True,help_text="Enter the number of hours you plan to stay")
    check_in_date = models.DateTimeField(auto_now_add=True)
    visit_status = models.CharField(max_length=20, choices=VISIT_STATUS, default='Waiting')

    def __str__(self):
        return self.full_name