from django.db import models
from django.contrib import admin
class Football (models.Model):
    name=models.CharField(max_length=100)
    salary=models.IntegerField()
    age=models.IntegerField()
    email=models.EmailField()
    goals=models.IntegerField()
class FootballAdmin(admin.ModelAdmin):
    list_display=('name','salary','age','email','goals')
    