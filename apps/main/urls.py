from django.urls import path, include
from main import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('book/', views.PublicGroupListView.as_view(), name="postlist"),
    path('book/<int:pk>/', views.GroupDetailView.as_view(), name="postlist"),
    path('private/book/', views.GroupListView.as_view(), name="postlist"),
    path('article/', views.ArticleListView.as_view(), name="postlist"),
    path('article/<int:pk>/', views.ArticleEditView.as_view(), name="article"),
    path('article/create/', views.ArticleCreateView.as_view(), name="index"),
]