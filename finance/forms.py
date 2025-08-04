from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Transaction,Goal

class RegisterForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email','password1','password2']



class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields=['transaction_title','transaction_type','transaction_amount','transaction_date']


class GoalsForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields=['goal_name','goal_target_amount','goal_deadline']