from django.contrib import admin

from .models import Fish, Gear, Lake

# Register your models here.
admin.site.register(Fish)
admin.site.register(Gear)
admin.site.register(Lake)
