from django.db import models


class Transaction(models.Model):
    type = models.IntegerField()
    date = models.DateField()
    value = models.DecimalField(max_digits=8, decimal_places=2)
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
    hour = models.TimeField()
    store_owner = models.CharField(max_length=14)
    store_name = models.CharField(max_length=19)

    def __repr__(self):
        return f"<Transaction [{self.id}]"
