from django.db import models
from django.utils import timezone
from django.urls import reverse_lazy


# Create your models here.
class WebsiteCategory(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=2000)
    date_added = models.DateTimeField(editable=False, default=timezone.now)
    date_updated = models.DateTimeField(default=timezone.now)
    count = models.IntegerField(default=0)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name_plural = "Categories"

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()

        return super(WebsiteCategory, self).save(*args, **kwargs)


class Website(models.Model):
    url = models.TextField(max_length=2000)
    title = models.CharField(max_length=200, null=True)
    meta_description = models.CharField(max_length=200, null=True)
    alexa_rank = models.IntegerField(null=True)
    category = models.ForeignKey(WebsiteCategory, on_delete=models.CASCADE)
    date_added = models.DateTimeField(editable=False, default=timezone.now)
    date_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '{}'.format(self.url)

    class Meta:
        verbose_name_plural = "Websites"

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()

        return super(Website, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('website-detail-view', kwargs={'id': self.id})


class WebPage(models.Model):
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    url = models.TextField(max_length=2000, unique=True)
    title = models.CharField(max_length=200, null=True)
    meta_description = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(editable=False, default=timezone.now)
    date_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name_plural = "Webpages"

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()

        return super(WebPage, self).save(*args, **kwargs)