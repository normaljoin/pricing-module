from typing import Any
from django.contrib import admin
from .forms import ConfigAdminForm, DistanceBaseTierAdminForm
from .models import Config, DistanceAdditionalTier, DistanceBaseTier, DistanceBaseTierWeek, TimeTier, Waiting

# Pricing Config
class ConfigAdmin(admin.ModelAdmin):
    form = ConfigAdminForm
admin.site.register(Config, ConfigAdmin)

#Distance Base Tiers
@admin.register(DistanceBaseTier)
class DistanceBaseTierAdmin(admin.ModelAdmin):
    form = DistanceBaseTierAdminForm
    list_display = ('id', 'display_selected_days', 'config_key_id',)
    filter_horizontal = ('selected_days',)
    def display_selected_days(self, obj):
        return ', '.join([day.day for day in obj.selected_days.all()])
    
#Additional Distance Tier
admin.site.register(DistanceAdditionalTier) 

#Waiting Time Calc
admin.site.register(Waiting) 

admin.site.register(TimeTier)
