# from django import forms
from django.contrib import admin

from .models import MifareClassicCard, MifareClassicCardSector


class MifareClassicCardSectorInline(admin.TabularInline):
    model = MifareClassicCardSector
    verbose_name_plural = "Sectors"
    extra = 0
    fields = ("index", "key_a", "key_b")


@admin.register(MifareClassicCard)
class MifareClassicCardAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "uid",
        "type",
        "number",
        "nickname",
        "updated_at",
    )
    list_filter = ["type"]
    search_fields = ["uid", "number", "nickname"]
    inlines = [MifareClassicCardSectorInline]
