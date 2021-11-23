from django.contrib import admin
from .models import Blog
from .models import Write

# Register your models here.
admin.site.register(Blog)
admin.site.register(Write)