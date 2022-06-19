from django.contrib import admin
from watch_app.models import UserProfile, Neighborhood


# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['user']}),
        ('Bio', {'fields': ['bio']}),
        ('Phone', {'fields': ['phone']}),
        ('Block', {'fields': ['block']}),
        ('Neighborhood', {'fields': ['neighborhood']}),
        ('Photo', {'fields': ['photo']}),
    ]
    
admin.site.register(UserProfile, ProfileAdmin)

class NeighborhoodAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Location', {'fields': ['location']}),
        ('Occupants', {'fields': ['occupants']}),
        ('User', {'fields': ['user']}),
        # ('Business', {'fields': ['business']}),
    ]
    
admin.site.register(Neighborhood, NeighborhoodAdmin)