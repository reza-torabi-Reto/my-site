from django.contrib import admin
from . models import Article, Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('posision','title','slug','status')
    list_filter = ('status',)
    search_fields = ('title','slug')
    prepopulated_fields = {'slug':('title',)}
    
admin.site.register(Category, CategoryAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','slug','category_to_str','jpublish','status')
    list_filter = ('status',)
    search_fields = ('title','body')
    ordering = ['status','publish']
    prepopulated_fields = {'slug':('title',)}

    def category_to_str(self, obj):
        return "، ".join([category.title for category in obj.category.all() ])
        
    category_to_str.short_description = 'دسته‌بندی'
    

admin.site.register(Article, ArticleAdmin)