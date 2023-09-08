from django import forms
from django.core.exceptions import ValidationError

from .models import User, UserInfo, University


class RegisterForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput(attrs={'type': 'password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'type': 'password'}))

    class Meta:
        model = User
        fields = ("username", "email", "password", "password2")
    

    def clean(self):
        super().clean()
        password = self.cleaned_data["password"]
        password2 = self.cleaned_data["password2"]
        if password != password2:
            raise ValidationError({"password": "Пароли не совпали!"})
        if len(password) < 8:
            raise ValidationError({"password": "Пароль должен содержать как минимум 8 элементов!"})



class LoginForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput(attrs={'type': 'password'}))

    class Meta:
        model = User
        fields = ("username", "password")

    def clean_username(self):
        data = self.cleaned_data["username"]
        try:
            User.objects.get(username=data)
        except User.DoesNotExist:
            raise ValidationError({"username": "Такой пользователь не существует!"})
        
        return data



class UserBaseForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d']
    )
    

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "image",
            "date_of_birth",
            "about"
        )

    
        


class UserInfoForm(forms.ModelForm):

    education = forms.ModelMultipleChoiceField(
        queryset=University.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
    )
    
    class Meta:
        model = UserInfo
        fields = (
            "education",
            "work",
            "address",
            "country",
        )