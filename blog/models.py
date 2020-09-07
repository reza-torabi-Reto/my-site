from django.db import models
from django.urls import reverse
from account.models import User
from django.utils import timezone
from django.utils.html import format_html
from extensions.utils import jalali_convert, peersian_time
# ----->

# my Managers
class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')

class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)

# Category Model
class Category(models.Model):
    parent = models.ForeignKey('self', default = None, null=True, blank=True,on_delete=models.SET_NULL, related_name='children',verbose_name='زیردسته')
    title = models.CharField(max_length=200, verbose_name='سرنام دسته‌بندی')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='نامک دسته‌بندی')
    status = models.BooleanField(default=True, verbose_name="آیا نمایش داده شود؟")
    posision = models.IntegerField(verbose_name="چیدمان")
    class Meta:
        verbose_name = 'دسته‌بندی'
        verbose_name_plural = 'دسته‌بندی ها'
        ordering = ['parent__id', 'posision']

    def __str__(self):
        return self.title
    objects = CategoryManager()
    
# ----->

#  Article Model
class Article(models.Model):
    STATUS_CHOICES = (
        ('d','پیش‌نویس'),
        ('p','نمایش داده شده'),
    )
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='articles', verbose_name='نویسنده')
    category = models.ManyToManyField(Category, verbose_name = 'دسته‌بندی', related_name="articles")
    title = models.CharField(max_length=200, verbose_name ='سرنام')
    slug = models.SlugField(max_length=100,unique=True, verbose_name ='نامک')
    body = models.TextField(verbose_name ='نوشته')
    thumbnail = models.ImageField(upload_to='images', verbose_name ='فرتور')
    publish = models.DateTimeField(default=timezone.now,verbose_name ='تاریخ نمایش')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1,choices=STATUS_CHOICES, verbose_name ='وضعیت')


    class Meta:
        verbose_name = 'نگاشت'
        verbose_name_plural = 'نگاشت ها'
        ordering = ['-publish']


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("account:home")

    def jpublish(self):
        return jalali_convert(self.publish)
    
    def jTimepublish(self):
        return peersian_time(self.publish)    
    jpublish.short_description = 'تاریخ انتشار'

    def thumbnail_tag(self):
        return format_html("<img style='width:100px; height:50px;border-radius:5px;' src='{}'>".format(self.thumbnail.url))

    def category_to_str(self):
        return "، ".join([category.title for category in self.category.active()])
    
    category_to_str.short_description = 'دسته‌بندی'
    
    objects = ArticleManager()
# ----->