from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView, GenericAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .models import Article, GroupArticles
from . import serializers
from .permissions import IsAuthenticatedAndOwnerOrReadOnly
from .services import generate_url


class ArticleListView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        articles = Article.objects.all()
        serializer = serializers.ArticleListSerializer(articles, many=True)
        return Response(serializer.data)


class ArticleCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        article = serializers.ArticleCreateSerializer(data=request.data)
        if article.is_valid():
            article.save()
        return Response(status=201)


class ArticleEditView(GenericAPIView, UpdateModelMixin):
    queryset = Article.objects.all()
    serializer_class = serializers.ArticleCreateSerializer
    permission_classes = [IsAuthenticatedAndOwnerOrReadOnly]

    def get(self, request, pk):
        article = Article.objects.get(id=pk)
        serializer = serializers.ArticleDetailSerializer(article)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


# GroupArticles views
class PublicGroupListView(APIView):
    permission_classes = [IsAuthenticatedAndOwnerOrReadOnly]

    def get(self, request):
        groups = GroupArticles.objects.filter(private=False)
        serializer = serializers.GroupArticleListSerializer(groups, many=True)
        return Response(serializer.data)


class GroupListView(APIView):
    permission_classes = [IsAuthenticatedAndOwnerOrReadOnly]

    def get(self, request):
        groups = GroupArticles.objects.all()
        serializer = serializers.GroupArticleListSerializer(groups, many=True)
        return Response(serializer.data)


class GroupDetailView(APIView):
    def get(self, request, pk):
        group = GroupArticles.objects.get(id=pk)
        serializer = serializers.GroupArticleDetailSerializer(group)
        return Response(serializer.data)
# end