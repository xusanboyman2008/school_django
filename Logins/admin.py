from django.contrib import admin
from django.contrib.admin import site

from Logins.models import User,Logins_model
# Register your models here.
site.register(User)
site.register(Logins_model)