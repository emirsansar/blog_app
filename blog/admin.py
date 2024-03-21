from django.contrib import admin

# Register your models here.

from .models import Blog, Category

class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "is_home","slug")
    list_editable = ("is_active", "is_home")
    search_fields = ("title", "description")
    readonly_fields = ("slug",)
    list_filter = ("category","is_home","is_active",)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
