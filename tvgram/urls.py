"""tvgram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static 
from django.conf import settings
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', views.list, name='list'),
    path('detail/<int:show_id>/', views.detail, name='detail'),
    path('profile/<int:profile_id>/', views.profile, name='profile'),
    path('register/', views.user_register, name="register"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('update/<int:show_id>/', views.update, name="update"),
    path('delete/<int:show_id>/', views.delete, name='delete'),
    path('like/<int:show_id>/', views.like, name='like'),
    path('create/', views.create, name="create"),
    # path('create_profile/', views.create_profile, name="create_profile"),
    path('edit_profile/<int:profile_id>/', views.edit_profile, name="edit_profile"),
    # path('profiles/home/', views.home, name='profilehome'),
    path('search_user/', views.search_user, name='usersearch'),
    # path('follow/<int:follow_id>/', views.follow, name='follow'),
    path('contact/<int:user_to_id>/', views.contact, name='contact'),
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)