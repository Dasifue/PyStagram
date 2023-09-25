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
      

class ComentCreationForm(forms.ModelForm):
    class Meta:
        model= Comment
        fields=("text",)



class AnswerCommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields=(
            "text",
        )
        

class ComentUpdateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("text",)

