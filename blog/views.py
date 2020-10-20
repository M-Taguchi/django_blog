from django.shortcuts import render

from django.db.models import Count, Q
from django.http import Http404
from django.utils import timezone
from django.urls import reverse
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

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
        if post.is_public:
            post.published_date = timezone.now()
        post.save()
        return redirect('post_detail', pk=post.pk)
        

class PostUpdate(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_edit.html"

    def form_valid(self, form):
        post = form.save(commit=False)
        if post.is_public:
            if :
                post.updated_date = timezone.now()
            else:
                post.published_date = timezone.now()
        post.save()
        return redirect('post_detail', pk=post.pk)
        

class PostDelete(DeleteView):
    model = Post
    template_name = "blog/post_delete.html"

    success_url = '/'

class PostDetailView(DetailView):
    model = Post

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        current_user = self.request.user
        if not obj.is_public and not current_user.is_authenticated:
            raise Http404
        return obj

class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = super().get_queryset()
        current_user = self.request.user
        if current_user.is_authenticated:
            return queryset
        else:
            return Post.objects.filter(is_public=True).order_by('-published_date')

class CategoryListView(ListView):
    queryset = Category.objects.annotate(
        num_posts=Count('post', filter=Q(post__is_public=True)))


class TagListView(ListView):
    queryset = Tag.objects.annotate(num_posts=Count(
        'post', filter=Q(post__is_public=True)))

class CategoryPostView(ListView):
    model = Post
    template_name = 'blog/category_post.html'
    paginate_by = 10

    def get_queryset(self):
        category_name = self.kwargs['category_slug']
        self.category = get_object_or_404(Category, name=category_name)
        current_user = self.request.user
        if current_user.is_authenticated:
            qs = super().get_queryset().filter(category=self.category).order_by('-published_date')
        else:
            qs = super().get_queryset().filter(category=self.category, is_public=True).order_by('-published_date')
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context

class TagPostView(ListView):
    model = Post
    template_name = 'blog/tag_post.html'
    paginate_by = 10

    def get_queryset(self):
        tag_name = self.kwargs['tag_slug']
        self.tag = get_object_or_404(Tag, name=tag_name)
        current_user = self.request.user
        if current_user.is_authenticated:
            qs = super().get_queryset().filter(tags=self.tag).order_by('-published_date')
        else:
            qs = super().get_queryset().filter(tags=self.tag, is_public=True).order_by('-published_date')
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.tag
        return context

"""
def post_list(request):
    return render(request, 'blog/post_list.html', {})
"""