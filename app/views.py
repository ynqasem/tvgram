from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .forms import ShowForm, UserRegisterForm, LoginForm, ProfileForm
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import Show, Like, Profile, Contact
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def like(request, show_id):
	show_obj = Show.objects.get(id=show_id)

	like_obj, created = Like.objects.get_or_create(user=request.user, show=show_obj)

	if created:
		action="like"
	else:
		action="unlike"
		like_obj.delete()

	like_count = show_obj.like_set.all().count()

	context = {
	"action": action,
	"count": like_count
	}
	return JsonResponse(context, safe=False)

def contact(request, user_to_id):
	user_to_obj = Profile.objects.get(id=user_to_id)

	follow_obj, created = Contact.objects.get_or_create(user_from=request.user, user_to=user_to_obj.user)

	if created:
		action="follow"
	else:
		action="unfollow"
		follow_obj.delete()

	follow_count = user_to_obj.user.rel_to_set.all().count()

	context = {
	"action": action,
	"count": follow_count
	}
	return JsonResponse(context, safe=False)


# def follow(request, follow_id):
#     follow_obj = Profile.objects.get(id=follow_id)

#     follow_obj, created = Follow.objects.get_or_create(user=request.user, followers=follow_obj)

#     if created:
#         action="follow"
#     else:
#         action="unfollow"
#         like_obj.delete()

#     follow_count = follow_obj.follow_set.all().count()

#     context = {
#     "action": action,
#     "count": follow_count
#     }
#     return JsonResponse(context, safe=False)

def user_login(request):
	form = LoginForm()
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			my_username = form.cleaned_data['username']
			my_password = form.cleaned_data['password']
			auth_user = authenticate(username=my_username, password=my_password)
			if auth_user is not None:
				login(request, auth_user)
				return redirect("profile", profile_id=auth_user.profile.id)
	context = {
		"form": form
	}
	return render(request, 'login.html', context)


def user_logout(request):
	logout(request)
	return redirect('login')

def list(request):
	if not request.user.is_authenticated:
		return redirect('login')

	object_list = Show.objects.all()
	object_list = object_list.order_by('publish_date', 'name', 'username')
	query = request.GET.get('q')
	if query:
		object_list = object_list.filter(name__contains=query)
	

	liked_shows = []
	# following_list = []
	likes = request.user.like_set.all()
	for like in likes:
		liked_shows.append(like.show)
	context = {
	"shows": object_list,
	"my_likes": liked_shows,
	# "my_following": following_list,


	}
	return render(request, 'list.html', context)

def update(request, show_id):
	if not request.user.is_authenticated:
		return redirect('login')
	if not (request.user.is_staff or request.user==Show.username):
		return HttpResponse("you're not the username or the staff. You are not allowed to edit this post")
	show_obj = Show.objects.get(id=show_id)
	form = ShowForm(instance=show_obj)
	if request.method == "POST":
		form = ShowForm(request.POST, request.FILES or None, instance = show_obj,)
		if form.is_valid():
			form.save()
			return redirect("detail", show_id=show_obj.id)
	context = {
	"show_obj":show_obj,
	"update_form":form,

	}
	return render(request, 'update.html', context)


def delete(request, show_id):
	if not request.user.is_authenticated:
		return redirect('login')
	if not (request.user.is_staff):
		return HttpResponse("you are not staff, you cant delete this ")
	
	instance = get_object_or_404(Show, id=show_id)
	instance.delete()
	return redirect("list")

def detail(request, show_id):
	show_obj = Show.objects.get(id=show_id)
	context = {
	"show_obj": show_obj,

	}


	return render(request, 'detail.html', context)

def create(request):
	if not request.user.is_authenticated:
		return redirect('login')
	form = ShowForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		post = form.save(commit = False)
		post.username = request.user
		post.save()
		return redirect("list")
	context = {
	"create_form":form,
	}

	return render(request, 'create.html', context)




# def create_profile(request):
# 	if not request.user.is_authenticated:
# 		return redirect('login')
# 	form = ProfileForm(request.POST or None, request.FILES or None)
# 	if form.is_valid():
# 		post = form.save(commit = False)
# 		post.user = request.user
# 		post.save()
# 		return redirect("list")
# 	context = {
# 	"create_form":form,
# 	}

# 	return render(request, 'create_profile.html', context)

def profile(request, profile_id):
	profile = Profile.objects.get(user=User.objects.get(id=profile_id))
	profile_obj = Profile.objects.get(id=profile_id)
	following_list = []
	context = {
	"profile_obj": profile_obj,
	"following_list": following_list

	}

	return render(request, 'profile.html', context)

def edit_profile(request, profile_id):
	if not request.user.is_authenticated:
		return redirect('login')
	if not (request.user.is_staff or request.user.profile.id==profile_id):
		return HttpResponse("you're not the username or the staff. You are not allowed to edit this profile")
	profile_obj = Profile.objects.get(id=profile_id)
	form = ProfileForm(instance=profile_obj)
	if request.method == "POST":
		form = ProfileForm(request.POST, request.FILES or None, instance = profile_obj,)
		if form.is_valid():
			form.save()
			return redirect("profile", profile_id=profile_obj.id)
	context = {
	"profile_obj":profile_obj,
	"profile_form":form,

	}
	return render(request, 'edit_profile.html', context)

def user_register(request):
	form = UserRegisterForm()
	if request.method == "POST":
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			person = form.save(commit=False)
			person.set_password(person.password)
			person.save()
			my_username = form.cleaned_data['username']
			my_password = form.cleaned_data['password']
			login(request, person)
			profile_obj = Profile.objects.create(user=person)
			return redirect('edit_profile', profile_id=profile_obj.id)
	context = {
		"form": form
	}
	return render(request, 'register.html', context)

def search_user(request):
	if not request.user.is_authenticated:
		return redirect('login')

	object_list = Profile.objects.all()
	object_list = object_list.order_by('user')
	query = request.GET.get('q')
	if query:
		object_list = object_list.filter(user__username__contains=query)

	follow_list = []
	# following_list = []
	follows = request.user.rel_to_set.all()
	for follow in follows:
		follow_list.append(follow.user_to)

	context = {
	"object_list":object_list,
	"my_following": follow_list

	}
	return render(request, 'search_user.html', context)
	

