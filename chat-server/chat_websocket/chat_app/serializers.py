from rest_framework import serializers
from chat_app.models import Userinfo
# from rest_framework.authtoken.models import Token


class Userinfo_data(serializers.ModelSerializer):
    class Meta:
        model = Userinfo
        fields = [
            'nickName', 'avatar', 'area', 'description', 'github', 'socialSite',
            'phone', 'email', 'website', 'id'
        ]
