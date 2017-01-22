from django import template
from mezzanine.blog.models import BlogPost, BlogCategory

register = template.Library()

@register.filter(name='has_category')
def has_category(blog_post):
    for category in categories:
        if category.title == 'Laos':
            return blog_post
