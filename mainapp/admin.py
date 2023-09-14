from django.contrib import admin

# Register your models here.
from .models import Clock
admin.site.register(Clock)