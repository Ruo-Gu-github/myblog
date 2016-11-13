from django.db import models
from django.utils import timezone
import datetime
from django.db.models import permalink


class Blogspost(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published',blank=True)
    body = models.TextField()
    url = models.URLField()
    publisher = models.CharField(max_length=200)
    def __unicode__(self):
        return self.title#, self.body, self.url, self.publisher
    def was_published_recently(self):
        now = timezone.now()
        return now >= self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
