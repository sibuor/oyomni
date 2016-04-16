from django.contrib import admin
from .import models

# Register your models here.
class EntryAdmin(admin.ModelAdmin):
	list_display = ["title", "created", "modified"]
	prepopulated_fields = {"slug":("title",)}

admin.site.register(models.Entry, EntryAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Comment)