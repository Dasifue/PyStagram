from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title', 
            'content',
            'image',
            'category_id',
        )
        
        

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            "title",
            "category_id",
            "image",
            "content",
        )
        # widgets = {
        #     "owner": forms.TextInput(attrs={}),
        #     "title": forms.TextInput(attrs={}),
        #     "content": forms.TextInput(attrs={}),
        #     "published": forms.DateInput(attrs={'type': 'date'}),
        #     "updated": forms.DateInput(attrs={'type': 'date'}),
        # }

class ComentCreationForm(forms.ModelForm):
    class Meta:
        model= Comment
        fields=("text",)
