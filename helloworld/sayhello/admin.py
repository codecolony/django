from django.contrib import admin

# Register your models here.
from .models import SayHello

class SayHelloAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Person Name',               {'fields': ['person_name']}),
    ]

admin.site.register(SayHello)