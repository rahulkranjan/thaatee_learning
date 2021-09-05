from django.db import models
from django.core.validators import *
from django.utils.text import slugify
from users.models import User
from django_mysql.models import JSONField, Model


class LmsCategory(models.Model):
    category_name = models.CharField(max_length=200, blank=True)
    category_image = models.ImageField(
        upload_to='images/', blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    origin = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    facts = models.TextField(blank=True)
    popular = models.BooleanField(default=False)
    display_home = models.BooleanField(default=False)
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
                    slug_exits = LmsCategory.objects.get(slug=slug)
                    if slug_exits:
                        slug = self.slug + '_' + str(counter)
                        counter += 1
                except LmsCategory.DoesNotExist:
                    self.slug = slug
                    break
        super(LmsCategory, self).save(*args, **kwargs)

    class Meta:
        db_table = 'lms_category'

    def __str__(self):
        return str(self.category_name)


class LmsSubCategory(models.Model):
    subcategory_name = models.CharField(max_length=150, blank=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    created_at = models.DateField(auto_now_add=True, auto_now=False)
    modified_at = models.DateField(auto_now_add=False, auto_now=True)
    status = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id and not self.slug:
            slug = slugify(self.subcategory_name)
            slug_exists = True
            counter = 1
            self.slug = slug
            while slug_exists:
                try:
                    slug_exits = LmsSubCategory.objects.get(slug=slug)
                    if slug_exits:
                        slug = self.slug + '_' + str(counter)
                        counter += 1
                except LmsSubCategory.DoesNotExist:
                    self.slug = slug
                    break
        super(LmsSubCategory, self).save(*args, **kwargs)

    class Meta:
        db_table = 'lms_sub_category'

    def __str__(self):
        return str(self.subcategory_name)


class Courses(models.Model):
    commission_type_choice = (
        ('Percentage', 'Percentage'),
        ('Amount', 'Amount'),

    )
    level_type_choice = (
        ('beginner', 'BEGINNER'),
        ('advanced', 'ADVANCED'),
        ('intermidate', 'INTERMIDATE')
    )

    course_name = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    course_image = models.ImageField(
        upload_to='images/', blank=True, null=True)
    category = models.ForeignKey(LmsCategory, on_delete=models.PROTECT)
    subcategory = models.ForeignKey(LmsSubCategory, on_delete=models.PROTECT)
    level_type = models.CharField(
        max_length=20, choices=level_type_choice, default='beginner')
    requirements = models.TextField(blank=True)
    short_description = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True)
    insturctor = models.ForeignKey(
        User, on_delete=models.PROTECT)
    course_price = models.IntegerField(default=0, blank=True)
    commission_type = models.CharField(
        max_length=20, choices=commission_type_choice, default='Amount')
    commission_fee = models.FloatField(default=0)
    seo_title = models.CharField(max_length=100, blank=True)
    seo_description = models.CharField(max_length=100, blank=True)
    seo_keyword = models.CharField(max_length=100, blank=True)
    course_price = models.IntegerField(blank=True, null=True)
    selling_price = models.IntegerField(blank=True, null=True)
    popular = models.BooleanField(default=False)
    display_home = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True, auto_now=False)
    modified_at = models.DateField(auto_now_add=False, auto_now=True)
    status = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id and not self.slug:
            slug = slugify(self.course_name)
            slug_exists = True
            counter = 1
            self.slug = slug
            while slug_exists:
                try:
                    slug_exits = Courses.objects.get(slug=slug)
                    if slug_exits:
                        slug = self.slug + '_' + str(counter)
                        counter += 1
                except Courses.DoesNotExist:
                    self.slug = slug
                    break
        super(Courses, self).save(*args, **kwargs)

    class Meta:
        db_table = 'courses'

    def __str__(self):
        return str(self.course_name)


class RateCourse(models.Model):
    courses = models.ForeignKey(Courses,
                                on_delete=models.PROTECT)
    user = models.ForeignKey(User,
                             on_delete=models.PROTECT)
    rate = models.IntegerField(default=5, validators=[MaxValueValidator(5),
                                                      MinValueValidator(1)])
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True, auto_now=False)

    class Meta:
        db_table = 'rate_course'

    def __str__(self):
        return str(self.courses)


class CourseSection(models.Model):

    course = models.ForeignKey(
        Courses, on_delete=models.PROTECT, limit_choices_to={'status': True})
    section_name = models.TextField(blank=True, null=True)
    section_position = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'course_section'

    def __str__(self):
        return str(self.section_name)


class KeyHiglight(models.Model):
    course = models.ForeignKey(
        Courses, on_delete=models.PROTECT)
    position = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    highlight_img = models.FileField(upload_to='files/', blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'key_highlights'

    def __str__(self):
        return str(self.course)


class Lesson(models.Model):
    type_choices = (
        ('document', 'DOCUMENT'),
        ('youtubelink', 'YOUTUBELINK'),
        ('embeddedlink', 'EMBEDDEDLINK'),
        ('link', 'LINK'),

    )
    content_type = models.CharField(
        max_length=300, choices=type_choices)
    course_section = models.ForeignKey(
        CourseSection, on_delete=models.PROTECT, limit_choices_to={'status': True})
    lesson_name = models.TextField(blank=True, null=True)
    lesson_icon = models.ImageField(
        upload_to='images/', blank=True, null=True)
    lesson_position = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    lesson_duration = models.CharField(max_length=50, blank=True, null=True)
    document = models.FileField(upload_to='files/', blank=True, null=True)
    upload_Video = models.ImageField(
        upload_to='video/', blank=True, null=True)
    video_link = models.URLField(blank=True, null=True)
    youtube_link = models.URLField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    embedded_link = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'lesson'

    def __str__(self):
        return str(self.lesson_name)


class Quiz(models.Model):
    quiz_title = models.TextField(blank=True, null=True)
    course_section = models.ForeignKey(
        CourseSection, on_delete=models.PROTECT, blank=True, null=True, limit_choices_to={'status': True})
    instructions = models.TextField(null=True, blank=True)
    passing_percentage = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'quiz'

    def __str__(self):
        return str(self.quiz_title)


class Questions(Model):
    question_title = models.TextField(blank=True, null=True,)
    quiz = models.ForeignKey(
        Quiz, on_delete=models.PROTECT, blank=True, null=True, limit_choices_to={'status': True})
    no_of_option = models.IntegerField(blank=True, null=True)
    options = JSONField()
    hint = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'questions'

    def __str__(self):
        return str(self.question_title)


class ProgressHistory(models.Model):

    user = models.ForeignKey(User, blank=True, null=True,
                             on_delete=models.PROTECT, limit_choices_to={'is_active': True})
    progress = models.BooleanField(default=False)
    course = models.ForeignKey(
        Courses, on_delete=models.PROTECT, limit_choices_to={'status': True})
    course_section = models.ForeignKey(
        CourseSection, on_delete=models.PROTECT, blank=True, null=True, limit_choices_to={'status': True})
    # lesson = models.ForeignKey(Lesson, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        db_table = 'progress_history'

    def __str__(self):
        return str(self.user)


class Enrolled(models.Model):
    user = models.ForeignKey(User, blank=True, null=True,
                             on_delete=models.PROTECT, limit_choices_to={'is_active': True})
    course = models.ForeignKey(
        Courses, on_delete=models.PROTECT, limit_choices_to={'status': True})
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        db_table = 'enrolled'

    def __str__(self):
        return str(self.user)+str(self.course)
