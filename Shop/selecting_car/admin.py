from django.contrib import admin
from . import models

@admin.register(models.SelectCar)
class CarAdmin(admin.ModelAdmin):
    pass

# Register your models here.
