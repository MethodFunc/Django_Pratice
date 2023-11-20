from django.conf import settings
from django.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator


# Create your models here.

class Post(models.Model):
    # models.GenericIPAddressField
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField(
        # 유효성 검사 최소 10단어 이상
        validators=[MinLengthValidator(10)]

    )
    photo = models.ImageField(blank=True, upload_to='instagram/post/%Y/'
                                                    '%m/%d')
    tag_set = models.ManyToManyField('Tag', blank=True)
    is_public = models.BooleanField(default=False, verbose_name="공개 여부")
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # return f"Post Object: {self.id}"
        return self.message

    def get_absolute_url(self):
        return reverse("instagram:post_detail", args=[self.pk])

    class Meta:
        ordering = ['-id']

    # def message_length(self):
    #     return len(self.message)
    #
    # message_length.short_description = "메세지 글자 수


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, limit_choices_to={'is_public': True})
    message = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    # post_set = models.ManyToManyField(Post)

    def __str__(self):
        return self.name
