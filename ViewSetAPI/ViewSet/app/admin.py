from django.contrib import admin
from .models import Car
# Register your models here.

@admin.register((Car))
class CarModelAdmin(admin.ModelAdmin):
    list_display=['id','name','color','model','prize']