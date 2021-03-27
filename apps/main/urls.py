from django.urls import path, include
from main.views import (
	ArticleListView, 
	ArticleDetailView,
    ArticleCreateView,
	ArticleEditView,
	)
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('article/', ArticleListView.as_view(), name="postlist"),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name="article"),
    path('article/edit/<int:pk>/', ArticleEditView.as_view(), name="article"),
    path('article/create/', ArticleCreateView.as_view(), name="index"),
]