from django.contrib import admin

from .models import Show, Like, Profile, Contact

admin.site.register(Show)
admin.site.register(Like)
admin.site.register(Profile)
admin.site.register(Contact)

# admin.site.register(Follow)
