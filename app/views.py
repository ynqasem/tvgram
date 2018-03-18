from django.shortcuts import render

from .models import Show 


def list(request):
	show_obj = Show.objects.all()
	context = {
		"show_obj": show_obj
	}
	return render(request, 'list.html', context)

def detail(request, show_id):
	show_obj = Show.objects.get(id=show_id)
	context = {
		"show_obj": show_obj
	}
	return render(request, 'detail.html', context)

