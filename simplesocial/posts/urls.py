from django.urls import path, re_path
from posts import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostListView.as_view(), name='all'),
    path('new/', views.CreatePostView.as_view(), name='create'),
    re_path(r'by/(?P<username>[-\w]+)', views.UserPostView.as_view(), name='for_user'),
    re_path(r'by/(?P<username>[-\w]+)/(?P<pk>\d+)/$', views.PostDetailView.as_view(), name='single'),
    re_path(r'delete/(?P<pk>\d+)/$', views.DeletePostView.as_view(), name='delete'),
]
