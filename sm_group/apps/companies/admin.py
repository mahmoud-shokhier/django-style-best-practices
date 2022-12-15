from django.contrib import admin
from .models import Company
# Register your models here.
@admin.register(Company)
class Companydmin(admin.ModelAdmin):
    list_display = ("id", "name", "updated_at", "start_date", "end_date")
    list_filter = ("name", "updated_at")
    search_fields = ("name",)
    date_hierarchy = "updated_at"
