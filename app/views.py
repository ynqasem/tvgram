from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import ShowForm, UserRegisterForm, LoginForm, ProfileForm
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import Show, Like




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
				return redirect("list")
	context = {
		"form": form
	}
	return render(request, 'login.html', context)

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
			return redirect("list")
	context = {
		"form": form
	}
	return render(request, 'register.html', context)

def user_logout(request):
    logout(request)
    return redirect('login')

def list(request):
	if not request.user.is_authenticated:
		return redirect('login')
	object_list = Show.objects.all()
	object_list = object_list.order_by('publish_date', 'name')
	query = request.GET.get('q')
	if query:
		object_list = object_list.filter(name__contains=query)

	liked_shows = []
	likes = request.user.like_set.all()
	for like in likes:
		liked_shows.append(like.show)
	context = {
	"shows": object_list,
	"my_likes": liked_shows,

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
	# messages.success(request, "Successfully Deleted!")
	return redirect("list")

def detail(request, show_id):
	show_obj = Show.objects.get(id=show_id)
	# items = Item.objects.filter(restaurant=show_obj)
	context = {
	"show_obj": show_obj,
	# "items": items

	}


	return render(request, 'detail.html', context)

def create(request):
	if not request.user.is_authenticated:
		return redirect('login')
	form = ShowForm()
	if request.method == "POST":
		form = ShowForm(request.POST, request.FILES or None)
		if form.is_valid():
			form.save()
			return redirect("list")
	context = {
	"create_form":form,
	}

	return render(request, 'create.html', context)


def following(request, user_id):
	following_list = Following.objects.get(id=user_id)

	following_obj, created = Following.objects.get_or_create(user=request.user, show=following_list)

	if created:
		action="follow"
	else:
		action="unfollow"
		following_obj.delete()

	following_count = following_list.following_set.all().count()

	context = {
	"action": action,
	"count": following_count
	}
	return JsonResponse(context, safe=False)

