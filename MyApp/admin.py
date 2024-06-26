from django.contrib import admin
from .models import Complains,Pricing,Daily_Usage
# Register your models here.

class ComplainsAdmin(admin.ModelAdmin):
    list_display = ('email', 'phonenumber', 'complain', 'comments', 'date')

admin.site.register(Complains, ComplainsAdmin)
admin.site.register(Daily_Usage)
admin.site.register(Pricing)