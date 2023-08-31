from django.db import models

# Create your models here.
class Board(models.Model):
    bno = models.CharField(max_length=8, primary_key=True)
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=8)
    cno = models.CharField(max_length=8)
    allerinfo = models.CharField(max_length=200, null=True)
    cdate = models.DateField()
    content = models.CharField(max_length=500)

class Comment(models.Model):
    bno = models.CharField(max_length=8, primary_key=True)
    cno = models.CharField(max_length=8)
    cdate = models.DateField()