# from django import  forms
# from django.forms import TextInput, ImageField, DateField, NumberInput, Select


# class PostUpdateForm(forms.ModelForm):
#     class Meta:
#         fields=(
#             "owner",
#             "title",
#             "image",
#             "content",
#             "published",
#             "updated",
#             )
#         widgets={
#             "owner": forms.TextInput(
#                 attrs={}
#             ),
#             "tittle": forms.TextInput(
#                 attrs={}
#             ),
#             # "image": forms.ImageField(
#             #     attrs={"class": "custom-image-input"}

            
#             "content" : forms.TextInput(
#                 attrs={}
#             ),
#             "published": forms.DateField(
#                 attrs={"type": "date"}
#             ),
#             "updated": forms.DateField(
#                 attrs={"type": "date"}
#             ),
#         }


    
from django import forms

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
