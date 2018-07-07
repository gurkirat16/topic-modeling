from django.contrib import admin

# Register your models here.

from uploads.core.models import EngineData

class EngineDataAdmin(admin.ModelAdmin):
    search_fields = ('word', 'appear_time')
    list_display = ('word', 'appear_time')
    ordering = ('-appear_time',)


admin.site.register(EngineData, EngineDataAdmin)

