from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from .models import Userinfo
from .serializers import Userinfo_data

HostUrl = 'http://127.0.0.1:9000/upload/'


# 登录
@api_view(['POST'])
def dchat_login(request):
    username = request.POST['username']
    password = request.POST['password']

    user = User.objects.filter(username=username)

    if user:
        isnotUser = check_password(password, user[0].password)
        if isnotUser:
            token = Token.objects.get_or_create(user=user[0])
            token = Token.objects.get(user=user[0]).key
            return Response(token)
        else:
            return Response('pwd arr')
    else:
        return Response('user none')


# 退出登录
# 退出登录后将Token表中相关的token删除
@api_view(['POST'])
def dchat_logout(request):
    token = request.POST['token']
    user_token = Token.objects.get(key=token)
    user_token.delete()
    return Response('logout')


@api_view(['POST'])
def userinfo(request):
    token = request.POST['token']
    user = Token.objects.get(key=token).user
    userinfo = Userinfo.objects.get(belong=user)
    userinfo_data = {
        "nickName": userinfo.nickName,
        "avatar": HostUrl + str(userinfo.avatar),
        "area": userinfo.area,
        "description": userinfo.description,
        "github": userinfo.github,
        "socialSite": userinfo.socialSite,
        "phone": userinfo.phone,
        "email": userinfo.email,
        "website": userinfo.website,
    }

    # print(userinfo_data)

    return Response(userinfo_data)


class Userinfo_view(APIView):
    def get(self, request, format=None):
        userinfo = Userinfo.objects.all()
        userinfo_data = []
        for user in userinfo:
            user_item = {
                "nickName": user.nickName,
                "avatar": HostUrl + str(user.avatar),
                "description": user.description,
            }
            userinfo_data.append(user_item)

        return Response(userinfo_data)
        # return Response('userinfo-get')

    def post(self, request, format=None):
        token = request.POST['token']
        # print('user token')
        # print(token)
        if token:
            # 获取token列表
            token_data = Token.objects.filter(key=token)
            if token_data:
                # user = Token.objects.get(key=token).user
                user = token_data[0].user
                # userinfo = Userinfo.objects.get(belong=user)
                userinfo = Userinfo.objects.filter(belong=user)

                userinfo_data = Userinfo_data(userinfo, many=True).data[0]

            # if userinfo_data.is_valid():
            #     return Response(userinfo_data.data)
            # else:
            #     return Response(userinfo_data.errors)
            else:
                userinfo_data = {
                    "nickName": "未登录",
                    "avatar": HostUrl + "default/user.jpg",
                    "area": "",
                    "description": "",
                    "github": "",
                    "socialSite": "",
                    "phone": "",
                    "email": "",
                    "website": "",
                }

        else:
            userinfo_data = {
                "nickName": "未登录",
                "avatar": HostUrl + "default/user.jpg",
                "area": "",
                "description": "",
                "github": "",
                "socialSite": "",
                "phone": "",
                "email": "",
                "website": "",
            }
            # print(userinfo_data)
        # 返回用户列表 取其一
        return Response(userinfo_data)