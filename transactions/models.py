from django.db import models


class Transactions(models.Model):
    from_acc = models.ForeignKey("accounts.User", on_delete=models.SET_NULL, related_name='transaction_from', null=True)
    to_acc = models.ForeignKey("accounts.User", on_delete=models.SET_NULL, related_name='transaction_to', null=True)
    amount = models.PositiveIntegerField()

# t = Transactions.objects.filter(from_acc=user)
#  ikkalasi bir xil bittasi realated name bilan
# t = user.transaction_from.all()
