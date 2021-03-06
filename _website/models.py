from django.db import models
from django.utils.timezone import now
from django.utils import translation

from martor.models import MartorField

from .utils import *

class Site(models.Model):
    display_name = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=20)

    custom_css = models.TextField(blank=True, null=True)
    custom_js = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.name


class MenuItem(MultilingualModel):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    title_tr = models.CharField(max_length=100)
    title_en = models.CharField(max_length=100)

    order = models.PositiveIntegerField(default=1)

    redirect_link = models.CharField(max_length=1000, default='', blank=True)

    class Meta:
        ordering = ['site', 'order']

    def __str__(self):
        return '{} - {} - {}'.format(self.site.name, self.order, self.name)


class FlatPage(MultilingualModel):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    redirect_link = models.CharField(max_length=1000, default='', blank=True)

    title_tr = models.CharField(max_length=100, blank=True, null=True)
    title_en = models.CharField(max_length=100, blank=True, null=True)

    content_tr = MartorField(blank=True, null=True)
    content_en = MartorField(blank=True, null=True)

    blank_page = models.BooleanField(default=False)

    home_page_order = models.PositiveIntegerField(default=0, help_text='Make 0 to hide in home page')

    class Meta:
        ordering = ['site', 'name', '-pk']

    def __str__(self):
        return '{} - {}'.format(self.site.name, self.name)


class CarouselItem(MultilingualModel):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)

    title_tr = models.CharField(max_length=100, blank=True)
    title_en = models.CharField(max_length=100, blank=True)

    subtitle_tr = models.CharField(max_length=100, blank=True)
    subtitle_en = models.CharField(max_length=100, blank=True)

    image = models.ImageField()

    class Meta:
        ordering = ['site', '-pk']

    def __str__(self):
        return '{} - {} - {}'.format(self.site.name, self.title, self.pk)


class Event(MultilingualModel):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)

    title_tr = models.CharField(max_length=40)
    title_en = models.CharField(max_length=40)

    content_tr = MartorField()
    content_en = MartorField()

    class Meta:
        ordering = ['site', '-pk']

    def __str__(self):
        return '{} - {}'.format(self.site.name, self.title)


class EventImage(models.Model):
    event = models.ForeignKey(Event, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField()


class Announcement(MultilingualModel):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)

    title_tr = models.CharField(max_length=40)
    title_en = models.CharField(max_length=40)

    content_tr = MartorField()
    content_en = MartorField()

    image = models.ImageField(blank=True, null=True)

    class Meta:
        ordering = ['site', '-pk']

    def __str__(self):
        return '{} - {}'.format(self.site.name, self.title)


class UsefulLink(MultilingualModel):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)

    title_tr = models.CharField(max_length=300)
    title_en = models.CharField(max_length=300)

    icon = models.CharField(max_length=20, blank=True, null=True, default='book')
    url = models.URLField()

    def __str__(self):
        return '{} - {}'.format(self.site.name, self.title)


class ContestLanguage(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)

    name = models.CharField(max_length=20)

    class Meta:
        ordering = ['site', 'name', '-pk']

    def __str__(self):
        return '{} - {}'.format(self.site.name, self.name)


class ContestRule(MultilingualModel):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)

    order = models.PositiveIntegerField(default=0)

    content_tr = models.TextField()
    content_en = models.TextField()

    class Meta:
        ordering = ['site', 'order', '-pk']

    def __str__(self):
        return '{} - {}'.format(self.site.name, self.content)


class FAQItem(MultilingualModel):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)

    order = models.PositiveIntegerField(default=0)

    content_tr = models.TextField()
    content_en = models.TextField()

    answer_tr = models.TextField()
    answer_en = models.TextField()

    class Meta:
        ordering = ['site', 'order', '-pk']

    def __str__(self):
        return '{} - {}'.format(self.site.name, self.content)
