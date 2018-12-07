from django.db import models

# Create your models here.
class computer_science_view(models.Model):
    view=models.IntegerField(default=1)

class current_affairs_view(models.Model):
    view=models.IntegerField(default=1)

class general_knowledge_view(models.Model):
    view=models.IntegerField(default=1)

class general_science_view(models.Model):
    view=models.IntegerField(default=1)

class government_exam_view(models.Model):
    view=models.IntegerField(default=1)