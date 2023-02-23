from django import template
import timeago, datetime, pytz
from ..models import Dog
from django.db.models import Count
import markdown
from django.utils.safestring import mark_safe

register = template.Library()
import readtime
@register.filter
def read_time(text):
    return str(readtime.of_text(text))

@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))		

