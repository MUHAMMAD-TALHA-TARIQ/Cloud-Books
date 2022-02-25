from django.contrib import admin
from .models import *


# Books Section Admin (BS_admin)
@admin.register(Books_Section)
class BS_admin(admin.ModelAdmin):
    list_display = ['parent_id', 'self_id', 'heading']
