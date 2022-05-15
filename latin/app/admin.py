from django.contrib import admin

from .models import *


class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'lang')
    list_display_links = ('name', 'lang')
    prepopulated_fields = {"slug": ("name",)}
    save_on_top = True


class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Country, CountryAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Religion)
admin.site.register(Politition)
admin.site.register(Language)
admin.site.register(CountryShots)
