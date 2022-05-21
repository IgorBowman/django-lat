from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class CountryShotsInline(admin.TabularInline):
    model = CountryShots
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="120"')

    get_image.short_description = "Изображение"


class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'lang')
    list_display_links = ('name',)
    readonly_fields = ("get_image",)
    prepopulated_fields = {"slug": ("name",)}
    save_on_top = True
    inlines = [CountryShotsInline, ]

    list_filter = ("lang",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photos.url} width="100" height="110"')

    get_image.short_description = "Изображение"


class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Country, CountryAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Religion)
admin.site.register(Politition)
admin.site.register(Language)
admin.site.register(CountryShots)
