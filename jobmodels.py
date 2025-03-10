from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    website = models.URLField(blank=True)

    def _str_(self):
        return self.name

class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    location = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=[('Tech', 'Tech'), ('Finance', 'Finance'), ('Marketing', 'Marketing')])
    posted_date = models.DateTimeField(auto_now_add=True)
    employer = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)

    def _str_(self):
        return self.title
