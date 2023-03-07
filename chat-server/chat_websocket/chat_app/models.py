import os
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Userinfo(models.Model):
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join('Users', self.nickName, instance)
        return None

    nickName = models.CharField(null=True, blank=True, max_length=80)
    avatar = models.ImageField(default='default/user.jpg',
                               upload_to=image_upload_to,
                               max_length=255)
    area = models.CharField(null=True, blank=True, max_length=80)
    description = models.TextField('Description',
                                   max_length=600,
                                   default='',
                                   blank=True)
    github = models.CharField(null=True, blank=True, max_length=200)
    socialSite = models.CharField(null=True, blank=True, max_length=200)
    phone = models.CharField(null=True, blank=True, max_length=200)
    email = models.EmailField(unique=True)
    website = models.CharField(null=True, blank=True, max_length=200)
    belong = models.OneToOneField(User,
                                  on_delete=models.CASCADE,
                                  related_name='userinfo_user',
                                  null=True,
                                  blank=True)

    def __int__(self):
        return self.id
