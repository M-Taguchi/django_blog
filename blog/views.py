from django.shortcuts import render

from django.db.models import Count, Q
from django.http import Http404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from blog.models import Post, Category, Tag


# Create your views here.

class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'

class CategoryListView(ListView):
    queryset = Category.objects.annotate(
        num_posts=Count('post', filter=Q(post__is_public=True)))

class TagListView(ListView):
    queryset = Tag.objects.annotate(
        num_posts=Count('post', filter=Q(post__is_public=True)))

"""
def post_list(request):
    return render(request, 'blog/post_list.html', {})
"""