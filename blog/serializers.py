from rest_framework import serializers

from .models import Post

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'link', 'link_name', 'content', 'date_posted', 'author')