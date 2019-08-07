from django.db import models


class Degree(models.Model):
    degreeName = models.CharField(max_length=50, unique=True, verbose_name='Degree Name')

    class Meta:
        verbose_name_plural = 'Degree'

    def __str__(self):
        return self.degreeName




class Subject(models.Model):
    id = models.CharField(max_length=10, verbose_name='Course Code',primary_key=True)
    couseName = models.CharField(max_length=50, verbose_name='Course Name')
    credit = models.IntegerField()

    def __str__(self):
        return self.id + " - " + self.couseName