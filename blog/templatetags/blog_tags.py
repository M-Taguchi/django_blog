from django import template
from django.db.models import Count, Q
from blog.models import Category, Tag

register = template.Library()


@register.inclusion_tag('includes/category_links.html')
def render_category_links():
    return {
        'categories_list': Category.objects.annotate(num_posts=Count('post', filter=Q(post__is_public=True))),
    }

@register.inclusion_tag('includes/tag_links.html')
def render_category_links():
    return {
        'tags_list': Tag.objects.annotate(num_posts=Count('post', filter=Q(post__is_public=True))),
    }