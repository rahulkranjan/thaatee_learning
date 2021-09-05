from django.db import models
from django.core.validators import *
from django.utils.text import slugify
from users.models import User


class Category(models.Model):
    category_name = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(max_length=100, unique=True)
    created_at = models.DateField(auto_now_add=True, auto_now=False)
    modified_at = models.DateField(auto_now_add=False, auto_now=True)
    status = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id and not self.slug:
            slug = slugify(self.category_name)
            slug_exists = True
            counter = 1
            self.slug = slug
            while slug_exists:
                try:
                    slug_exits = Category.objects.get(slug=slug)
                    if slug_exits:
                        slug = self.slug + '_' + str(counter)
                        counter += 1
                except Category.DoesNotExist:
                    self.slug = slug
                    break
        super(Category, self).save(*args, **kwargs)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return str(self.category_name)


class SubCategory(models.Model):
    subcategory_name = models.CharField(max_length=100, blank=True)
    created_at = models.DateField(auto_now_add=True, auto_now=False)
    modified_at = models.DateField(auto_now_add=False, auto_now=True)
    status = models.BooleanField(default=True)
    slug = models.SlugField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        if not self.id and not self.slug:
            slug = slugify(self.subcategory_name)
            slug_exists = True
            counter = 1
            self.slug = slug
            while slug_exists:
                try:
                    slug_exits = SubCategory.objects.get(slug=slug)
                    if slug_exits:
                        slug = self.slug + '_' + str(counter)
                        counter += 1
                except SubCategory.DoesNotExist:
                    self.slug = slug
                    break
        super(SubCategory, self).save(*args, **kwargs)

    class Meta:
        db_table = 'sub_category'

    def __str__(self):
        return str(self.subcategory_name)


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    blog_title = models.CharField(max_length=500)
    blog_image = models.ImageField(
        upload_to='images/', default='', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.PROTECT)
    content = models.TextField(blank=True)
    seo_title = models.CharField(max_length=200, blank=True, null=True)
    seo_keyword = models.CharField(max_length=200, blank=True, null=True)
    seo_description = models.CharField(max_length=200, blank=True, null=True)
    status = models.BooleanField(default=True)
    popular = models.BooleanField(default=False)
    slug = models.SlugField(max_length=100, unique=True)
    viwes_count = models.IntegerField(default=0)
    created_at = models.DateField(auto_now_add=True, auto_now=False)
    modified_at = models.DateField(auto_now_add=False, auto_now=True)

    def save(self, *args, **kwargs):
        if not self.id and not self.slug:
            slug = slugify(self.blog_title)
            slug_exists = True
            counter = 1
            self.slug = slug
            while slug_exists:
                try:
                    slug_exits = Blog.objects.get(slug=slug)
                    if slug_exits:
                        slug = self.slug + '_' + str(counter)
                        counter += 1
                except Blog.DoesNotExist:
                    self.slug = slug
                    break
        super(Blog, self).save(*args, **kwargs)

    class Meta:
        db_table = 'blog'

    def __str__(self):
        return str(self.blog_title)


class Rate(models.Model):
    blog = models.ForeignKey(Blog,
                             on_delete=models.PROTECT, limit_choices_to={'status': True})
    user = models.ForeignKey(User,
                             on_delete=models.PROTECT)
    rate = models.IntegerField(default=5, validators=[MaxValueValidator(5),
                                                      MinValueValidator(1)])
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True, auto_now=False)

    class Meta:
        db_table = 'rate'

    def __str__(self):
        return str(self.blog)


class Events(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    slug = models.SlugField(max_length=100, blank=True)
    event_title = models.CharField(max_length=500)
    event_image = models.ImageField(
        upload_to='images/', default='', blank=True, null=True)
    event_description = models.CharField(
        max_length=1000, blank=True, null=True)
    small_description = models.CharField(max_length=200, blank=True, null=True)
    event_location = models.CharField(max_length=1000)
    event_price = models.IntegerField(default=0)
    event_date = models.DateField()
    event_time = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True, auto_now=False)
    modified_at = models.DateField(auto_now_add=False, auto_now=True)
    status = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id and not self.slug:
            slug = slugify(self.event_title)
            slug_exists = True
            counter = 1
            self.slug = slug
            while slug_exists:
                try:
                    slug_exits = Events.objects.get(slug=slug)
                    if slug_exits:
                        slug = self.slug + '_' + str(counter)
                        counter += 1
                except Events.DoesNotExist:
                    self.slug = slug
                    break
        super(Events, self).save(*args, **kwargs)

    class Meta:
        db_table = 'events'

    def __str__(self):
        return str(self.event_title)
