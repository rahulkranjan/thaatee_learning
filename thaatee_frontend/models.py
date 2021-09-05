from django.db import models
from django.utils.text import slugify
from django.conf import settings
User = settings.AUTH_USER_MODEL

# Create your models here.


class Pages(models.Model):
    name = models.CharField(max_length=100, default='', blank=True, null=True)
    seo_title = models.CharField(max_length=100, blank=True)
    seo_description = models.CharField(max_length=100, blank=True)
    seo_keyword = models.CharField(max_length=100, blank=True)
    page_content = models.TextField(default='', blank=True, null=True)
    slug = models.SlugField(max_length=100, unique=True)
    created_at = models.DateField(auto_now_add=True, auto_now=False)
    modified_at = models.DateField(auto_now_add=False, auto_now=True)
    status = models.BooleanField(default=True)
    page_count = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.id and not self.slug:
            slug = slugify(self.name)
            slug_exists = True
            counter = 1
            self.slug = slug
            while slug_exists:
                try:
                    slug_exits = Pages.objects.get(slug=slug)
                    if slug_exits:
                        slug = self.slug + '_' + str(counter)
                        counter += 1
                except Pages.DoesNotExist:
                    self.slug = slug
                    break
        super(Pages, self).save(*args, **kwargs)

    class Meta:
        db_table = 'pages'

    def __str__(self):
        return str(self.name)


class ImgGallery(models.Model):
    name = models.CharField(max_length=100, default='', blank=True, null=True)
    product_image = models.ImageField(
        upload_to='images/', default='', blank=True, null=True)
    created_at = models.DateField(auto_now_add=True, auto_now=False)
    modified_at = models.DateField(auto_now_add=False, auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'img_gallery'

    def __str__(self):
        return str(self.name)


class HomeSlide(models.Model):
    name = models.CharField(max_length=100, default='', blank=True, null=True)
    description = models.CharField(
        max_length=1000, default='', blank=True, null=True)
    product_image = models.ImageField(
        upload_to='images/', default='', blank=True, null=True)
    urls = models.URLField(blank=True, null=True)
    position = models.IntegerField(default='0')
    created_at = models.DateField(auto_now_add=True, auto_now=False)
    modified_at = models.DateField(auto_now_add=False, auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'home_slider'

    def __str__(self):
        return str(self.name)


class OfferSlide(models.Model):
    name = models.CharField(max_length=100, default='', blank=True, null=True)
    description = models.CharField(
        max_length=1000, default='', blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    product_image = models.ImageField(
        upload_to='images/', default='', blank=True, null=True)
    position = models.IntegerField(default='0')
    created_at = models.DateField(auto_now_add=True, auto_now=False)
    modified_at = models.DateField(auto_now_add=False, auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'Offer_Slide'

    def __str__(self):
        return str(self.name)


class Testimonials(models.Model):
    name = models.CharField(max_length=100, default='', blank=True, null=True)
    client_image = models.ImageField(
        upload_to='testimonials/', default='', blank=True, null=True)
    client_testimonials = models.TextField(
        default='', blank=True, null=True)
    home_status = models.BooleanField(default=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'testimonials'

    def __str__(self):
        return str(self.name)


class Contact(models.Model):
    name = models.CharField(max_length=100, default='', blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True)
    phone = models.BigIntegerField(default=0)
    message = models.CharField(
        max_length=1000, default='', blank=True, null=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'contact'

    def __str__(self):
        return str(self.name)


class Faq(models.Model):
    title = models.CharField(
        max_length=1000, default='', blank=True, null=True)
    discription = models.TextField(blank=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'faq'

    def __str__(self):
        return str(self.name)


class Subscribe(models.Model):
    email = models.EmailField(unique=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'subscribe'

    def __str__(self):
        return str(self.email)


class ContactInstructor(models.Model):
    name = models.CharField(max_length=100, default='', blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True)
    user = models.ForeignKey(User,
                             on_delete=models.PROTECT)
    phone = models.BigIntegerField(default=0)
    message = models.CharField(
        max_length=1000, default='', blank=True, null=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'contact_instructor'

    def __str__(self):
        return str(self.name)
