from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    description=models.TextField(blank=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    priority_choices = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low')
    ]
    name = models.CharField(max_length=100, primary_key=True)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    priority = models.CharField(max_length=20)
    attach_file = models.FileField(upload_to='attachment', null=True, blank=True)
    # assignees = models.ManyToManyField(User, related_name='assigned_to', null=True, blank=True)
    # your_instance = YourModel.objects.create()
    # your_instance.assignees.add(user1, user2, user3)