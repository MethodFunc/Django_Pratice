import random
from django import forms
from .models import Profile
from django.contrib.auth.forms import AuthenticationForm


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["email", "zipcode"]


class LoginForm(AuthenticationForm):
    q1 = random.randint(0, 10)
    q2 = random.randint(0, 10)
    answer = forms.IntegerField(help_text=f"{q1} + {q2} = ?")

    def clean_answer(self):
        answer = self.cleaned_data.get("answer")
        if answer != self.q1 + self.q2:
            raise forms.ValidationError("Answer is not correct.")
        return answer