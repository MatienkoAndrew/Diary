from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Diary(models.Model):
	YES_NO = (("Да", "Да"), ("Нет", "Нет"))

	worker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	created_date = models.DateTimeField(default=timezone.now())
	published_date = models.DateTimeField(blank=True, null=True)
	author = models.CharField(max_length=100, default='Матиенко Андрей Павлович')
	title = models.CharField(max_length=200, default="Просто хороший день", blank=True)
	aim = models.CharField(max_length=200)
	action = models.TextField()
	good_things = models.TextField()
	bad_things = models.TextField()
	new_thing = models.TextField()
	thanks = models.TextField()
	charity = models.DecimalField(max_digits=15, decimal_places=2, default=0)
	strength = models.TextField()
	tomorrow = models.TextField()
	morning = models.CharField(max_length=20, choices=YES_NO, default='Нет')
	bed = models.CharField(max_length=20, choices=YES_NO, default='Нет')
	arrange = models.CharField(max_length=20, choices=YES_NO, default='Нет')
	dishware = models.CharField(max_length=20, choices=YES_NO, default='Нет')
	done = models.CharField(max_length=20, choices=YES_NO, default='Нет')
	work_time = models.CharField(max_length=20, choices=YES_NO, default='Нет')
	PE = models.CharField(max_length=20, choices=YES_NO, default='Нет')
	meditation = models.CharField(max_length=20, choices=YES_NO, default='Нет')

	def	publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title