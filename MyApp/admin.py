from django.contrib import admin
from .models import Complains
from .models import Usage

# Register your models here.

class ComplainsAdmin(admin.ModelAdmin):
    list_display = ('email', 'phonenumber', 'complain', 'comments', 'date')

admin.site.register(Complains, ComplainsAdmin)
admin.site.register(Usage)