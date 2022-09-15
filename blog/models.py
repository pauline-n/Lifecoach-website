from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

# Create your models here.
class BlogPage(Page):
    heading = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=100)
    body = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('heading'),
        FieldPanel('author'),
        FieldPanel('body')
    ]