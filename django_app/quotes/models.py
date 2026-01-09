from django.db import models

class Quote(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=100)
    tags = models.CharField(max_length=200)
    author_profile = models.URLField()

    def __str__(self):
        return self.author
