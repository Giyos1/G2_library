from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.urls import reverse
from django.views import View

from accounts.forms import UserForm, LoginForm, FileUploadForm, ForgotPasswordForm, RestorePasswordForm
from accounts.models import UploadFile, User, Code
from accounts.service import send_email_thread


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get("password"))
            user.save()
            return redirect('books_list')
        return render(request, 'accounts/register.html', {'form': form})
    elif request.method == 'GET':
        form = UserForm()
        return render(request, 'accounts/register.html', {'form': form})


def login_user(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get("user")
            login(request, user)
            return redirect('books_list')
        return render(request, 'accounts/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('accounts:login')


def file_upload(request):
    if request.method == 'POST':

        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('accounts:file_list')
        return render(request, 'file/file_upload.html', {'form': form})
    form = FileUploadForm()
    return render(request, 'file/file_upload.html', {'form': form})


def file_list(request):
    files = UploadFile.objects.all()
    return render(request, 'file/list.html', {'files': files})


class ForgotPassword(View):
    def get(self, request):
        form = ForgotPasswordForm()
        return render(request,
                      'accounts/forgot_password.html',
                      {'form': form})

    def post(self, request):
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            user = User.objects.filter(username=form.cleaned_data.get('username')).first()
            code = Code.objects.create(
                user=user
            )
            send_email_thread(
                subject='parolni tiklash',
                message=f'Code:{code.code}',
                #         f'<a href="http://127.0.0.1:8000{reverse('accounts:restore_password')}?username={user.username}" class="button">Link</a>',
                to_email=user.email
            )
            return render(request, 'accounts/done.html')
        return render(request,
                      'accounts/forgot_password.html',
                      {'form': form})


class RestorePassword(View):
    def get(self, request):
        form = RestorePasswordForm()
        return render(request, 'accounts/restore.html', {'form': form})

    def post(self, request):
        form = RestorePasswordForm(data=request.POST, username=request.GET.get('username'))
        if form.is_valid():
            user = form.cleaned_data.get('user')
            user.set_password(form.cleaned_data.get('password'))
            return redirect('accounts:login')
        return render(request, 'accounts/restore.html', {'form': form})
