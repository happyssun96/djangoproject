from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    userschool = models.CharField(max_length=32, verbose_name = '소속')
    useremail = models.EmailField(max_length=128, verbose_name = '이메일')
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name = '가입시간')

class Blog(models.Model):
    title= models.CharField(max_length=100, verbose_name = '제목')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name = '게시일시')
    body= models.TextField(max_length=5000, verbose_name = '내용')

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:100]