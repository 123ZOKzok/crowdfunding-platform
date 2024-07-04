# projects/models.py
from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    goal_amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    # Add more fields as needed

class Donation(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    donated_at = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(Project, related_name='donations', on_delete=models.CASCADE)
    donor = models.ForeignKey(User, on_delete=models.CASCADE)
    # Add more fields as needed

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    # Add more fields as needed

