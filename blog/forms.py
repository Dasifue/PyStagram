from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        
        

class PostUpdateForm(forms.ModelForm):
    class Meta:
        fields = (
            "owner",
            "title",
            "image",
            "content",
            "published",
            "updated",
        )
        widgets = {
            "owner": forms.TextInput(attrs={}),
            "title": forms.TextInput(attrs={}),
            "content": forms.TextInput(attrs={}),
            "published": forms.DateInput(attrs={'type': 'date'}),
            "updated": forms.DateInput(attrs={'type': 'date'}),
        }
