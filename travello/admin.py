from django.contrib import admin
from .models import Destinations
# Register your models here.
admin.site.register(Destinations)
# it is only after registering our models that we can be able to manipulate or add objects to our database
