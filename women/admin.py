from django.contrib import admin
from . import models


@admin.register(models.Women)
class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

