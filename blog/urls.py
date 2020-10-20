from django.urls import path

from .views import IndexView, PostDetailView, PostNew, PostUpdate, PostDelete, CategoryListView, TagListView, CategoryPostView, TagPostView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostNew.as_view(), name='post_new'),
    path('post/<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('tags/', TagListView.as_view(), name='tag_list'),
    path('categories/<str:category_slug>/',
         CategoryPostView.as_view(), name='category_post'),
    path('tags/<str:tag_slug>/', TagPostView.as_view(), name='tag_post'),
]