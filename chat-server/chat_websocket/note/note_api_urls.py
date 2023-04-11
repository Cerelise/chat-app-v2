from django.urls import path
from note import note_apis

urlpatterns = [
    path('add-article/', note_apis.add_article),
    path('update-article/', note_apis.update_article),
    path('get-userArticle/', note_apis.get_userArticle),
    path('article_img/', note_apis.article_img),
    path('article/', note_apis.article_view),
]
