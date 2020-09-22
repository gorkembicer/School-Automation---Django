from django.contrib import admin
from .models import student

admin.site.site_header = "PAULİS ADMİN PANELİ"

@admin.register(student)
class studentAdmin(admin.ModelAdmin):

    list_display = ["name","surname","author","phone","gender","created_date"]
    list_display_links = ["name","surname","author","phone","gender","created_date"]
    list_filter = ["created_date"]

    search_fields = ["name","surname"]


    class Meta: #django tarafından söylenen bişey değiştirilemez.
        model = student
