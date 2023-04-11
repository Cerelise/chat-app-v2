from rest_framework import serializers
from chat_app.models import Userinfo


class ArticleSerializers(serializers.ModelSerializer):
    title = serializers.CharField(max_length=50)
    desc = serializers.CharField(max_length=200, source="subtitle")
    content = serializers.TextField()
    published = serializers.DateField()

    def create(self, validated_data):

        return super().create(validated_data)