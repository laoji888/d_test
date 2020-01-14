from django.db import models

# Create your models here.
class Grades(models.Model):
    gname = models.CharField(max_length=20)
    adate = models.DateTimeField()
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()
    isdelete = models.BooleanField(default=False)


class students(models.Model):
    sname = models.CharField(max_length=20)
    sgender = models.BooleanField()
    sage = models.IntegerField()
    scondent = models.CharField(max_length=20)
    isdelete = models.BooleanField(default=False)
    sgrade = models.ForeignKey("Grades")


