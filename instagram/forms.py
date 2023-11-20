import re
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        #  추천하지 않음, 특정필드를 배재하지만 새로운 필드를 추가 시 노출 이 됨
        # exclude = ["Author"]
        fields = [
            "message", "photo","tag_set", "is_public"
        ]

    # Post 저장 시 message에 존재하는 영어 문자열 제거
    # def clean_message(self):
    #     message = self.cleaned_data.get("message")
    #     if message:
    #         message = re.sub(r"[a-zA-Z]", '', message)
    #     return message
