from django.contrib import admin

from items.models import Item


@admin.register(Item)
class ItemModelAdmin(admin.ModelAdmin):
    list_display = admin.ModelAdmin.list_display + (
        'name',
        'slug',
        'hash_id',

        'created_at',
        'updated_at',
    )

    list_filter = admin.ModelAdmin.list_filter + (
        'site',
    )

    inlines = (
    )

    search_fields = (
        'name',
        'slug',
        'hash_id',
    )

    readonly_fields = (
        'created_at',
        'updated_at',
    )
