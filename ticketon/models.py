from django.db import models
from django.forms import forms


class User(models.Model):
	login = models.CharField(max_length = 50)
	password = models.CharField(max_length = 50)

class  Movie(models.Model):
        name = models.CharField(max_length = 50)
        description = models.TextField(max_length = 150)
        rating = models.IntegerField()

class Cinema(models.Model):
        name = models.CharField(max_length = 50)

class Schedule(models.Model):
        time = models.DateField()
        hall  = models.IntegerField()
        cinema_name = models.ForeignKey('Cinema', on_delete=models.CASCADE, null=True)
        movie_name = models.ForeignKey('Movie', on_delete=models.CASCADE, null=True)


#
class Tickets(models.Model):
    schedule = models.ForeignKey('Schedule', on_delete=models.CASCADE, null=True)
    seat = models.IntegerField()
    available = models.BooleanField()
    user = models.ForeignKey('User', on_delete=models.CASCADE, null=True)

