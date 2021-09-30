from django.contrib import admin

# Register your models here.
from .models import   Producto, categoria

admin.site.register(categoria)
admin.site.register(Producto)