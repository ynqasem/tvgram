from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator



class Show(models.Model):
	name = models.CharField(max_length=220)
	image = models.ImageField(null=True)
	username = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
	description = models.TextField()
	rating = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(5)])

	def __str__(self):
		return self.name

