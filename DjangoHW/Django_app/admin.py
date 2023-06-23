from django.contrib import admin
from Django_app.models import Informations
# Register your models here.

class InformationsAdmin(admin.ModelAdmin):
    list_display = ('First_name', 'Last_name', 'Product_id')  # veya fields = ('First_name', 'Last_name', 'Product_id')

admin.site.register(Informations, InformationsAdmin)