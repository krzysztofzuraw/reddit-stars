from django.db import models

class RedditLink(models.Model):
    title = models.CharField(max_length=250)
    url = models.URLField()
    is_favourite = models.BooleanField(default=False)
