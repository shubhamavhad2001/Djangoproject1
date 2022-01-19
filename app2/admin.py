from django.contrib import admin
from .models import Customer,product,student

# Register your models here.
class Studentadmin(admin.ModelAdmin):
    list_display=('names','roll','mobile','dept')
admin.site.register(Customer)
admin.site.register(product)
admin.site.register(student,Studentadmin)