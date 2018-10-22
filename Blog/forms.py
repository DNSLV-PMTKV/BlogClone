from django import forms
from django.contrib.auth.models import User
from .models import Post


class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('title', 'text')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'text_input_text'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }
