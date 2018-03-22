from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings

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

	def __str__(self):
		return '{} likes {}'.format(self.user, self.show)



class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(null=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	dob = models.DateField(auto_now=False, auto_now_add=False, null=True)
	about = models.CharField(max_length=500)

	def __str__(self):
		return 'Profile for user {}'.format(self.user.username)
	
# class Follow(models.Model):
#     following = models.ForeignKey(User, related_name="sheep", on_delete=models.CASCADE)
#     followers = models.ForeignKey(User, related_name="shephard", on_delete=models.CASCADE)

# class UserProfile(models.Model):
#     user = models.ForeignKey(User, unique = True, related_name = 'user', on_delete=models.CASCADE)
#     follows = models.ManyToManyField('self', related_name='follows', symmetrical=False, on_delete=models.CASCADE)



class Contact(models.Model):
	user_from = models.ForeignKey(User, related_name='rel_from_set', on_delete=models.CASCADE)
	user_to = models.ForeignKey(User, related_name='rel_to_set', on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True, db_index=True)

	class Meta:
		ordering = ('-created',)

	def __str__(self):
		return '{} follows {}'.format(self.user_from, self.user_to)

# Add following field to User dynamically

User.add_to_class('following', models.ManyToManyField('self', through=Contact, related_name='followers', symmetrical=False))
