from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo, Post


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoFrom(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = {}


class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('title', 'text')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'text_input_text'}),
            'text': forms.Textarea(attrs={'class': 'edible medium-editor-textarea postcontent'}),
        }
