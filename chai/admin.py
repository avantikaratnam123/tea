from django.contrib import admin
from . models import *

# Register your models here.
@admin.register((Contact))
class ContactModelAdmin(admin.ModelAdmin):
    list_display=['name','email','subject','message']

@admin.register((Product))
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id', 'description','upload_image']


