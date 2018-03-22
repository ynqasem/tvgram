from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator



class Show(models.Model):
	name = models.CharField(max_length=220)
	image = models.ImageField(null=True)
	username = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
	description = models.TextField()
	rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
	publish_date = models.DateField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.name

class Like(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	show = models.ForeignKey(Show, on_delete=models.CASCADE)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField(auto_now=False, auto_now_add=False, null=True)
    about = models.CharField(max_length=500)
    
# class Follow(models.Model):
#     following = models.ForeignKey(User, related_name="sheep", on_delete=models.CASCADE)
#     followers = models.ForeignKey(User, related_name="shephard", on_delete=models.CASCADE)




