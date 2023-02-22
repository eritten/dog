from django.db import models
from django.urls import reverse
from markdownfield.models import MarkdownField, RenderedMarkdownField
from markdownfield.models import MarkdownField, RenderedMarkdownField
from markdownfield.validators import VALIDATOR_STANDARD

# Create your models here.

class Dog(models.Model):
    name = models.CharField(max_length=100)
    age =models.PositiveIntegerField()
    picture = models.ImageField(upload_to="images")
    description = MarkdownField(rendered_field='text_rendered', validator=VALIDATOR_STANDARD)
    text_rendered = RenderedMarkdownField()

    breed = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('detail', args=(self.pk, self.name))

