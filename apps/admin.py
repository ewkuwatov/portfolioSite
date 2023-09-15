from django.contrib import admin
from .models import Testimonial, Team, Price, Contact

# Register your models here.
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'position']
    list_filter = ['name', 'position']

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'position']
    list_filter = ['name', 'position']

@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ['package_name', 'package_price']
    list_filter = ['package_name', 'package_price']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'number']
    list_filter = ['name', 'number']

