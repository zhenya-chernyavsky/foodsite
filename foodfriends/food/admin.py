from django.contrib import admin
from .models import Food, Category, Recipes
from django.utils.safestring import mark_safe


class FoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'create_at', 'update_at', 'get_photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published',)
    fields = ('title', 'content', 'photo', 'get_photo', 'is_published', 'create_at', 'update_at')
    readonly_fields = ('get_photo', 'create_at', 'update_at')
    save_on_top = True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        else:
            return 'нет фото'
    get_photo.short_description = 'Фото'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

class RecipesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

admin.site.register(Food, FoodAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Recipes, RecipesAdmin)
admin.site.site_title = 'Управление едой'
admin.site.site_header = 'Управление едой'