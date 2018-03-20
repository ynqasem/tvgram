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
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_img = models.ImageField(null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    about = models.CharField(max_length=500)
    # following = models.ForeignKey(User, on_delete=models.CASCADE)
    # followers = models.ForeignKey(User, on_delete=models.CASCADE)
    # posts = models.ForiegnKey(User, on_delete=models.CASCADE)


class Following(models.Model):
	user = models.ForeignKey(User,related_name="followers", on_delete=models.CASCADE)
	followed_user = models.ForeignKey(User, related_name="following", on_delete=models.CASCADE)

class Followers(models.Model):
	user = models.ForeignKey(User,related_name="followers2", on_delete=models.CASCADE)

class Posts(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)


