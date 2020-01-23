from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Diary(models.Model):
	worker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	created_date = models.DateTimeField(default=timezone.now())
	published_date = models.DateTimeField(blank=True, null=True)
	author = models.CharField(max_length=100, default='Матиенко Андрей Павлович')
	title = models.CharField(max_length=200, blank=True)
	aim = models.CharField(max_length=200)
	action = models.TextField()
	good_things = models.TextField()
	bad_things = models.TextField()
	new_thing = models.TextField()
	thanks = models.TextField()
	charity = models.DecimalField(max_digits=15, decimal_places=2, default=0)
	strength = models.TextField()
	tomorrow = models.TextField()

	def	publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title