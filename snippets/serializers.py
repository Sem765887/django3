from rest_framework import serializers

from .models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
   class Meta:
       model = Snippet
       fields = ['id', 'title', 'code', 'linenos', 'language', 'style']

class SnippetSerializer(serializers.ModelSerializer):
   owner = serializers.ReadOnlyField(source='owner.username')

   class Meta:
       model = Snippet
       fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner']