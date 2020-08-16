from django.contrib import admin
from . models import Article, Category

def make_published(modeladmin, request, queryset):
    rows_updated = queryset.update(status = 'p')
    if rows_updated == 1:
        message_bit = 'منتشر شد.'
    else:
        message_bit = 'منتشر شدند.'
    modeladmin.message_user(request, "{} جستار {}".format(rows_updated, message_bit))
make_published.short_description = 'انتشار جستارهای برگزیده'

def make_draft(modeladmin, request, queryset):
    rows_updated = queryset.update(status = 'd')
    if rows_updated == 1:
        message_bit = 'پیش‌نمایش شد.'
    else:
        message_bit = 'پیش‌نمایش شدند.'
    modeladmin.message_user(request, "{} جستار {}".format(rows_updated, message_bit))
make_draft.short_description = 'پیش‌نمایش شدن جستارهای برگزیده'

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('posision','title','slug','parent','status')
    list_filter = ('status',)
    search_fields = ('title','slug')
    prepopulated_fields = {'slug':('title',)}
    
admin.site.register(Category, CategoryAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'thumbnail_tag','slug','category_to_str','jpublish','status')
    list_filter = ('status',)
    search_fields = ('title','body')
    ordering = ['status','publish']
    prepopulated_fields = {'slug':('title',)}
    actions = [make_published, make_draft]

    def category_to_str(self, obj):
        return "، ".join([category.title for category in obj.category_published() ])
        
    category_to_str.short_description = 'دسته‌بندی'
    

admin.site.register(Article, ArticleAdmin)