from django.http import HttpResponse
from django.shortcuts import redirect

from accounts.models import RoleChoices


def login_required(func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return func(request, *args, **kwargs)

    return wrapper


def admin_perm(func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.groups.filter(name=RoleChoices.ADMIN):
                return func(request, *args, **kwargs)
        return HttpResponse('403 Forbidden')

    return wrapper


def librarian_perm(func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.groups.filter(name=RoleChoices.LIBRARIAN):
                return func(request, *args, **kwargs)
        return HttpResponse('403 Forbidden')

    return wrapper


# def required_perm(name):
#     def deco(func):
#         def wrapper(request, *args, **kwargs):
#             if request.user.has_perm('book.add_book'):
#                 return func(request, *args, **kwargs)
#             return HttpResponse('403 Forbidden')
#
#         return wrapper
#
#     return deco
