from django.db import models as m

from tinymce.models import HTMLField

class Info(m.Model):

    title = m.TextField()
    content = HTMLField()

    def __str__(self):

        return self.title

    class Meta:

        ordering = ['title']