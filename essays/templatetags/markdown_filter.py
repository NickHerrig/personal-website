from django import template
import markdown

register = template.Library()

@register.filter
def markdown_filter(content):
    return markdown.markdown(content, safe_mode='escape')
