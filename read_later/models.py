from django.db import models

class RedditLink(models.Model):
    title = models.CharField(max_length=250)
    is_favourite = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.is_favourite:
            super(RedditLink, self).save(*args, **kwargs)
