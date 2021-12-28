from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *

admin.site.site_header = 'AuTeam | Админ панель'


class TariffAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'speed', 'cloud', 'price', 'is_promotion']
    list_filter = ['speed', 'cloud', 'is_promotion']
    list_display_links = ['id', 'title']
    list_editable = ['is_promotion']


class UserTariffAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'phone_number', 'tariff', 'is_paid', 'engineer', 'is_active', 'enabled_at']
    list_filter = ['tariff', 'is_active']
    list_display_links = ['user']
    list_editable = ['tariff', 'is_paid', 'is_active']
    readonly_fields = ['user']
    search_fields = ['user__username']


class TariffHistoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'tariff', 'engineer', 'is_declined', 'disabled_at']
    list_filter = ['tariff', 'is_declined']
    list_display_links = ['user']
    readonly_fields = ['user', 'tariff']
    search_fields = ['user__username']


class ComplaintAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'subject', 'engineer', 'status', 'created_at']
    list_filter = ['status']
    list_display_links = ['id', 'user']
    list_editable = ['engineer', 'status']
    search_fields = ['user__username', 'engineer__username']


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone_number', 'status', 'created_at']
    list_filter = ['status']
    list_display_links = ['id', 'name']
    list_editable = ['status']
    search_fields = ['name']


admin.site.register(Tariff, TariffAdmin)
admin.site.register(UserTariff, UserTariffAdmin)
admin.site.register(TariffHistory, TariffHistoryAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Contact, ContactAdmin)
