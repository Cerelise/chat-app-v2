from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password, make_password
from .models import Userinfo
from .serializers import Userinfo_data
import os
import datetime

HostUrl = 'http://127.0.0.1:9000/upload/'
picUrl = 'http://127.0.0.1:9000'


def CurrentUserId(token):
    exists = Token.objects.filter(key=token).exists()
    if exists:
        id = Token.objects.filter(key=token).first().user_id
    else:
        id = 0
    return id


# 登录
@api_view(['POST'])
def dchat_login(request):
    username = request.POST['username']
    password = request.POST['password']

    user = User.objects.filter(username=username)

    if user:
        isnotUser = check_password(password, user[0].password)
        if isnotUser:
            Token.objects.filter(user=user[0]).delete()
            token = Token.objects.create(user=user[0])
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


# 注册
@api_view(['POST'])
def dchat_register(request):
    username = request.POST['username']
    password = request.POST['password']
    user = User.objects.filter(username=username)
    if user:
        return Response('this user is exist')
    else:
        new_password = make_password(password, username)
        new_user = User(username=username, password=new_password)
        new_user.save()
    token = Token.objects.get_or_create(user=new_user)
    token = Token.objects.get(user=new_user)

    userinfo = Userinfo.objects.get_or_create(nickName=username,
                                              belong=new_user)
    userinfo = Userinfo.objects.get(belong=new_user)

    userinfo_data = {
        'token': token.key,
        'nickName': userinfo.nickName,
        'avatar': HostUrl + "default/user.jpg"
    }

    return Response(userinfo_data)


# 重置密码
@api_view(['POST'])
def dchat_reset_pwd(request):
    username = request.POST['username']
    password = request.POST['password']
    user = User.objects.filter(username=username)
    if not user:
        return Response('user is not exist')
    else:
        new_password = make_password(password, username)
        User.objects.filter(username=username).update(password=new_password)
    return Response('ok')


@api_view(['POST'])
def update_userinfo(request):
    token = request.POST['token']
    id = CurrentUserId(token)
    nickName = request.POST['nickName']
    avatar = request.POST['avatar']
    area = request.POST['area']
    phone = request.POST['phone']
    email = request.POST['email']
    website = request.POST['website']
    desc = request.POST['desc']
    User.objects.filter(id=id).update(username=nickName)
    Userinfo.objects.filter(belong_id=id).update(area=area,
                                                 nickName=nickName,
                                                 description=desc,
                                                 phone=phone,
                                                 email=email,
                                                 website=website)
    return Response('ok')


@api_view(['POST'])
def user_info(request):
    avatar = request.POST['avatar']
    print(request.FILES)
    print(type(avatar))
    return Response('ok')


@api_view(['POST'])
def get_userinfo(request):
    token = request.POST['token']
    user = Token.objects.get(key=token).user
    userinfo = Userinfo.objects.get(belong=user)
    userinfo_data = {
        "nickName": userinfo.nickName,
        "avatar": HostUrl+str(userinfo.avatar),
        "area": userinfo.area,
        "description": userinfo.description,
        "github": userinfo.github,
        "socialSite": userinfo.socialSite,
        "phone": userinfo.phone,
        "email": userinfo.email,
        "website": userinfo.website,
        "id": userinfo.id
    }
    return Response(userinfo_data)


class Userinfo_view(APIView):
    def get(self, request, format=None):
        userinfo = Userinfo.objects.all()
        userinfo_data = Userinfo_data(userinfo, many=True).data
        for user in userinfo_data:
            user['avatar'] = picUrl + user['avatar']
        return Response(userinfo_data)
        # return Response('userinfo-get')
    def put(self, request, format=None):
        token = request.POST['token']
        id = CurrentUserId(token)

        print(request.data)
        nickName = request.POST['nickName']
        area = request.POST['area']
        phone = request.POST['phone']
        email = request.POST['email']
        website = request.POST['website']
        desc = request.POST['desc']
        User.objects.filter(id=id).update(username=nickName)
        Userinfo.objects.filter(belong_id=id).update(area=area,
                                                     nickName=nickName,
                                                     description=desc,
                                                     phone=phone,
                                                     email=email,
                                                     website=website)
        userinfo = Userinfo.objects.filter(belong_id=id).first()
        print(request.FILES.get("avatar"))
        if  request.FILES.get("avatar"):
          userinfo.avatar = request.FILES.get("avatar")
        userinfo.save()
        return Response('ok')

    def post(self, request, format=None):
        token = request.POST['token']
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