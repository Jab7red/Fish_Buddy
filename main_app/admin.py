from django.contrib import admin

from .models import Fish, Gear, Lake, Log

# Register your models here.
admin.site.register(Fish)
admin.site.register(Gear)
admin.site.register(Lake)
admin.site.register(Log)
