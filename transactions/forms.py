from django import forms

from transactions.models import Transactions


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = '__all__'
