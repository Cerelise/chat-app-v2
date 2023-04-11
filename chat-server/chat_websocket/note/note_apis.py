from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from .models import Article
from chat_app.models import Userinfo
import datetime
# import requests
import os
import json

hostUrl = 'http://127.0.0.1:9000'
picUrl = 'http://127.0.0.1:9000/upload/'


def CurrentUserId(token):
    exists = Token.objects.filter(key=token).exists()
    if exists:
        id = Token.objects.filter(key=token).first().user_id
    else:
        id = 0
    return id


def article_data(userId, article):
    data = {
        'title': article.title,
        'nickName': '',
        'id': article.id,
        'content': article.content,
        'desc': article.subtitle,
        'publish': article.published,
        'userAvatar': str(Userinfo.objects.get(id=article.belong_id).avatar),
        'belongUser': Userinfo.objects.get(id=article.belong_id).nickName,
    }
    article_user = article.belong
    userinfo = Userinfo.objects.get(belong=article_user)
    if userinfo.nickName:
        data['nickName'] = userinfo.nickName
    else:
        data['nickName'] = article_user.username
    return data


@api_view(['POST'])
def add_article(request):
    title = request.POST['title']
    desc = request.POST['desc']
    content = request.POST['contents']
    token = request.POST['token']
    id = CurrentUserId(token)
    user_token = Token.objects.filter(user_id=id).first()
    # print(user_token)
    # 保存文章
    article = Article.objects.create(title=title,
                                     subtitle=desc,
                                     content=content,
                                     belong=user_token.user)
    return Response('ok')


@api_view(['POST'])
def update_article(request):
    token = request.POST['token']
    articleId = request.POST['articleId']
    title = request.POST['title']
    desc = request.POST['desc']
    content = request.POST['content']
    id = CurrentUserId(token)
    user_token = Token.objects.filter(user_id=id).first()
    Article.objects.filter(id=articleId).update(title=title,
                                                subtitle=desc,
                                                content=content,
                                                belong=user_token.user)
    return Response('ok')


# markdown上传本地图片
@api_view(['POST', 'PUT'])
def article_img(request):
    src = request.data['imgnode']
    src.name = datetime.datetime.now().shifttime(
        '%Y%M%D%H%M%S') + '.' + src.name.split('.')[1]
    print(src.name)
    # image_url = os.path.join('upload',src.name).replace('\\','/')
    # f = open(image_url,mode='wb')
    # for chunk in src.chunks():
    #     f.write(chunk)
    # f.close()
    # print(image_url)
    # new_src = hostUrl + image_url

    # image_url = {'url':new_src}
    # return Response(image_url)
    return Response('ok')


@api_view(['GET'])
def get_userArticle(request):
    userId = request.GET['userId']
    if not userId:
        userId = 0
    articles = Article.objects.filter(belong_id=userId).all().order_by('id')
    # total = len(articles)
    articles_data = []
    for item in articles:
        data = article_data(userId, item)
        articles_data.append(data)
    # print(articles_data)
    return Response(articles_data)


@api_view(['GET'])
def article_view(request):
    article_id = request.GET['id']
    userId = request.GET['userId']
    if not userId:
        userId = 0
    article = Article.objects.get(id=article_id)
    userinfo = Userinfo.objects.get(id=article.belong_id)
    # Article.objects.filter(id=article_id).update(article.view + 1)
    article_data = {
        'id': article_id,
        'title': article.title,
        'desc': article.subtitle,
        'published': article.published,
        'content': article.content,
        'nickName': userinfo.nickName,
        'avatar': picUrl + str(userinfo.avatar),
        'belongUser': article.belong_id
    }

    return Response(article_data)