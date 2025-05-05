from django import forms
from django.core.exceptions import ValidationError

from books.models import Book


# class BookForm(forms.Form):
#     name = forms.CharField(max_length=200, widget=forms.TextInput(
#         attrs={
#             "class": "form-control"
#         }
#     ))
#     descriptions = forms.CharField(min_length=10, widget=forms.Textarea(
#         attrs={
#             "class": "form-control"
#         }
#     ))
#     price = forms.IntegerField(
#         widget=forms.NumberInput(
#             attrs={"class": "form-control",
#                    'placeholder': "raqam kiriting"}
#         )
#     )
#
#     def clean_name(self):
#         name = self.cleaned_data.get("name")
#         if Book.objects.filter(name=name).exists():
#             raise ValidationError("Already exists")
#         return name

# def clean_price(self):
#     if


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'descriptions', 'price', 'image', 'source']
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control"
            }),
            "descriptions": forms.Textarea(attrs={
                "class": "form-control"
            })
        }

    # def clean_name(self):
    #     name = self.cleaned_data.get("name")
    #     if Book.objects.filter(name=name).exists():
    #         raise ValidationError("Already exists")
    #     return name
