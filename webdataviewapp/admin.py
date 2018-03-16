from django.contrib import admin
from .models import Post
# Register your models here.

#관리자 페이지에서 만든 모델을 보기 위해서는 아래와 같이 모델(object)를 등록해야 한다.
admin.site.register(Post)
