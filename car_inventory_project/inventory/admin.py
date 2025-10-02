from django.contrib import admin
from .models import Car

class CarAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'year', 'price', 'is_available')  # Columns in table
    list_filter = ('make', 'year', 'is_available')  # Sidebar filters
    search_fields = ('make', 'model')  # Search bar
    ordering = ('year', 'make')  # Default sort order

admin.site.register(Car, CarAdmin)