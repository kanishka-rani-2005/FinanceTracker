from django.db import models
from django.contrib.auth.models import User


class Transaction(models.Model):
    TRANSACTION_TYPES=[
        ('income','Income'),
        ('expense','Expense')
    ]
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    transaction_date = models.DateField()
    transaction_title=models.CharField(max_length=255)
    transaction_type = models.CharField(max_length=10,choices=TRANSACTION_TYPES)
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.transaction_title