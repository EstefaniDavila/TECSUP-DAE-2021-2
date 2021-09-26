from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import  Cliente, Producto, categoria

admin.site.register(categoria)
admin.site.register(Producto)
admin.site.register(Cliente)