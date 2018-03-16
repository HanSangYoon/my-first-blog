from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    # author, title, text, created_date, published_date 모두 속성이다. Post라는 모델(object)를 설명하는  properties 이다.
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # publish는 method이고 이는 Post라는 모델(object)가 구동하는데에 쓰이는 함수이다.
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # __str__
    def __str__(self):
        return self.title
