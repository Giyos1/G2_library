from django.db import transaction
from django.shortcuts import render, redirect
from transactions.forms import TransactionForm
from transactions.models import Transactions


def list(request):
    transactions = Transactions.objects.all()
    return render(request, 'transactions/list.html', {'transactions': transactions})


@transaction.atomic
def create(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            from_acc = form.cleaned_data.get('from_acc')
            to_acc = form.cleaned_data.get('to_acc')

            to_acc.balance += form.cleaned_data.get('amount')
            to_acc.save()

            from_acc.balance -= form.cleaned_data.get('amount')
            if from_acc.balance < 0:
                form.add_error('from_acc', "Hisobingizda mablag' yetarli emas.")
                return render(request, 'transactions/create.html', {'form': form})
            from_acc.save()

            form.save()
            return redirect('tran:list')
        return render(request, 'transactions/create.html', {'form': form})
    else:
        form = TransactionForm()
        return render(request, 'transactions/create.html', {'form': form})


