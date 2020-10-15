from django.shortcuts import render

from django.db.models import Count, Q
from django.http import Http404
from django.utils import timezone
from django.shortcuts import redirect
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from blog.models import Post, Category, Tag
from blog.forms import PostForm


# Create your views here.
class PostNew(CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_edit.html"
    def form_valid(self, form):
        post = form.save(commit=False)
        post.created_date = timezone.now()
        post.save()
        return redirect('/')

class PostDetailView(DetailView):
    model = Post

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if not obj.is_public:
            raise Http404
        return obj

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