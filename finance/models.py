from django.db import models
from django.contrib.auth.models import User


class Transaction(models.Model):
    TRANSACTION_TYPES=[
        ('Income','Income'),
        ('Expense','Expense')
    ]
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    transaction_date = models.DateField()
    transaction_title=models.CharField(max_length=255)
    transaction_type = models.CharField(max_length=10,choices=TRANSACTION_TYPES)
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.transaction_title
    

class Goal(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    goal_name=models.CharField(max_length=100)
    goal_target_amount=models.DecimalField(max_digits=10, decimal_places=2)
    goal_deadline=models.DateField()


    def __str__(self):
        return self.goal_name
    
    

