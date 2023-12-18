from django.db import models

class Task(models.Model):
    Task_title = models.CharField(max_length=50)
    Task_description = models.TextField()
    Task_status = models.CharField(max_length=30)
    time = models.DateTimeField(auto_now_add=True)
    
