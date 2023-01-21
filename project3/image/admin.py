from django.contrib import admin
from .models import images

@admin.register(images)
class ImageAdmin(admin.ModelAdmin):
    list_display=['id','photo','date']
