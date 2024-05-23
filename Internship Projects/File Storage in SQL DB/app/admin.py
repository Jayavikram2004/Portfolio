from django.contrib import admin
from .models import MediaStore

class MediaStoreAdmin(admin.ModelAdmin):
    list_display = ('file_number', 'file_name', 'file_type', 'file_extension')
    list_filter = ('file_type', 'file_extension')
    search_fields = ('file_number', 'file_name')

admin.site.register(MediaStore, MediaStoreAdmin)
