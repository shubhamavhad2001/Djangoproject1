from django.contrib import admin
from . models import product,Offer
# Register your models here.
class productadmin(admin.ModelAdmin):
    list_display=('name','price','stock')

class offer_admin(admin.ModelAdmin):
    List_display=('code','Discount')
admin.site.register(product,productadmin)
admin.site.register(Offer,offer_admin)
