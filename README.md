# Ex02 Django ORM Web Application
## Devoloped by: CHIDROOP M J
## Reference Number: 25018548
## Date: 02/10/2025

## AIM
To develop a Django application to store and retrieve data from a Car Inventory Database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```python

admin.py

from django.contrib import admin
from .models import Car

class CarAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'year', 'price', 'is_available')  # Columns in table
    list_filter = ('make', 'year', 'is_available')  # Sidebar filters
    search_fields = ('make', 'model')  # Search bar
    ordering = ('year', 'make')  # Default sort order

admin.site.register(Car, CarAdmin)

models.py

from django.db import models

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"

```


## OUTPUT

![alt text](<Screenshot (24).png>)


## RESULT
Thus the program for creating car inventory database database using ORM hass been executed successfully
