from django.contrib.auth.models import User
from django.db import models
from django.db.models import permalink
from django.utils.timezone import now


class News(models.Model):
    title = models.CharField(max_length=200, blank=False)
    slug = models.SlugField()
    public = models.BooleanField(default=False)
    starred = models.BooleanField(default=False)
    author = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    published_data = models.DateTimeField(default=now, blank=False)
    text = models.TextField(blank=False)

    def __str__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return "news-detail", [self.slug, ]

    class Meta:
        verbose_name_plural = "News"
