from django.contrib import admin
from . models import Article, Category

# Admin header chhange
admin.site.site_header = 'بخش مدیریت وبلاگ'


def make_published(modeladmin, request, queryset):
    rows_updated = queryset.update(status='p')
    if rows_updated == 1:
        message_bit = 'منتشر شد.'
    else:
        message_bit = 'منتشر شدند.'
    modeladmin.message_user(
            request, "{} جستار {}".format(rows_updated, message_bit))


make_published.short_description = 'انتشار جستارهای برگزیده'


def make_draft(modeladmin, request, queryset):
    rows_updated = queryset.update(status='d')
    if rows_updated == 1:
        message_bit = 'پیش‌نمایش شد.'
    else:
        message_bit = 'پیش‌نمایش شدند.'
    modeladmin.message_user(
        request, "{} جستار {}".format(rows_updated, message_bit))

make_draft.short_description = 'پیش‌نمایش شدن جستارهای برگزیده'

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('posision', 'title', 'slug', 'parent', 'status')
    list_filter = ('status',)
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'thumbnail_tag', 'slug','author',
                    'category_to_str', 'jpublish', 'status')
    list_filter = ('status','author')
    search_fields = ('title', 'body')
    ordering = ['status', 'publish']
    prepopulated_fields = {'slug': ('title',)}
    actions = [make_published, make_draft]



admin.site.register(Article, ArticleAdmin)
