from django.contrib import admin

# Register your models here.
from region.models import Country, State


admin.site.register(Country)
admin.site.register(State)