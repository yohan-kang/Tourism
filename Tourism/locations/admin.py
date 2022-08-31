from django.contrib import admin

from locations.models import Location
# Register your models here.

class LocationAdmin(admin.ModelAdmin):
  # list_display = ['id', 'type', 'user',"name_of_place"]
  # list_display_links = ['id', 'type']
  # readonly_fields = ('id',)
  pass

admin.site.register(Location)
