from django.contrib import admin

from shop.models import Contact, OrderUpdate, Orders, Product

# Register your models here.
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(OrderUpdate)