from rest_framework import serializers

from .models import Article, GroupArticles


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'url']


class ArticleDetailSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field="username", read_only=True)
    
    class Meta:
        model = Article
        fields = '__all__'


class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


# GroupArticles views
class GroupArticleListSerializer(serializers.ModelSerializer):
    articles = serializers.SlugRelatedField(slug_field="url", many=True, read_only=True)
    
    class Meta:
        model = GroupArticles
        fields = ['name', 'articles', 'slug']


class GroupArticleDetailSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field="username", read_only=True)
    articles = serializers.SlugRelatedField(slug_field="url", many=True, read_only=True)

    class Meta:
        model = GroupArticles
        fields = '__all__'


class GroupArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupArticles
        fields = '__all__'
# end

# class GroupArticlesSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['name', 'description', 'author', 'articles', 'private', 'slug', 'created_date']