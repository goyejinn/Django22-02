from django.db import models
from django.contrib.auth.models import User
import os
# Create your models here.


class Post(models.Model) :
    title = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=100, blank=True)
    content = models.TextField()

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    # %Y : 2022를 표현, %y : 22만을 표현
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 추후 author 작성
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return f'[{self.pk}]{self.title}:: {self.author} : {self.created_at}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1] # -1은 맨마지막을 의미함
        # a.txt -> [a txt] 0, 1 ... 순서
        # b.docx -> b docx
        # c.xlsx -> c xlsx
        # a.b.c.txt -> a b c txt 맨마지막요소가 확장자임