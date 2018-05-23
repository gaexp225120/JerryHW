from django.db import models

# Create your models here.
class Person(models.Model):
	school_id = models.CharField(max_length=20)
	name = models.CharField(max_length=20)
	birth=models.CharField(max_length=20)
	is_boy=models.BooleanField(default=False)
	def __str__(self):
		return self.school_id