from django import forms
from .models import Show, Profile
from django.contrib.auth.models import User

class LoginForm(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput())

class UserRegisterForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'first_name', 'last_name', 'password']
		widgets = {
		"password": forms.PasswordInput()
		}

class ShowForm(forms.ModelForm):
	class Meta:
		model = Show
		fields = ['name', 'description', 'image', 'rating']

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['first_name', 'last_name', 'about', 'profile_img', 'dob']
		
		widgets = {
			"dob": forms.DateInput(attrs={"type":"date"})
		}
		
		
