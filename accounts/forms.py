from django.utils import timezone
from django.contrib.auth import authenticate
from accounts.models import User, UploadFile, Code
from django import forms
from django.core.exceptions import ValidationError


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password"
        ]

    # def save(self, commit=True):
    #     return User.objects.create_user(**self.cleaned_data)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField()

    def clean(self):
        data = self.cleaned_data
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)
        if not user:
            raise ValidationError('password yoki username xato kiritilgan')
        return {"user": user}


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = (
            "name",
            "file"
        )


class ForgotPasswordForm(forms.Form):
    username = forms.CharField(max_length=200)

    def clean(self):
        if not User.objects.filter(username=self.cleaned_data.get('username')).exists():
            raise ValidationError('bunaqa user mavjud emas')
        return self.cleaned_data


class RestorePasswordForm(forms.Form):
    code = forms.CharField(max_length=6)
    password = forms.CharField(max_length=100)
    re_password = forms.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        self.username = kwargs.pop('username', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        code = cleaned_data.get('code')
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')
        username = self.username

        user = User.objects.filter(username=username).first()
        code = Code.objects.filter(user=user, code=code, expired_date__gt=timezone.now()).first()
        if not user:
            raise ValidationError('user topilmadi')

        if not code:
            raise ValidationError('Code topilmadi')

        if password != re_password:
            raise ValidationError('Parollar bir xil emas')
        cleaned_data['user'] = user
        return cleaned_data
