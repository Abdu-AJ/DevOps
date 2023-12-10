from django.contrib import admin
from .models import Complains

# Register your models here.

class ComplainsAdmin(admin.ModelAdmin):
    list_display = ('email', 'phonenumber', 'complain', 'comments', 'date')  # Add 'date' here

admin.site.register(Complains, ComplainsAdmin)