from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    description = models.TextField()
    salary = models.IntegerField(blank=True, null=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_date = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.title

class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField(blank=True)
    applied_on = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.applicant.username} - {self.job.title}"
