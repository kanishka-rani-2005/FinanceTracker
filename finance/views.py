from django.shortcuts import render,redirect
from django.http  import HttpRequest
from django.views import View
from .forms import RegisterForm,TransactionForm,Transaction,Goal,GoalsForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum


class Home(LoginRequiredMixin,View):
    def get(self,request,*args,**kwargs):
        transaction=Transaction.objects.filter(user=request.user)
        goal=Goal.objects.filter(user=request.user)

        total_income = Transaction.objects.filter(
            user=request.user, transaction_type='Income'
        ).aggregate(total=Sum('transaction_amount'))['total'] or 0

        total_expenses = Transaction.objects.filter(
            user=request.user, transaction_type='Expense'
        ).aggregate(total=Sum('transaction_amount'))['total'] or 0
        
        net_savings=total_income-total_expenses

        context={
            'transaction':transaction,
            'goal':goal,
            'total_income':total_income,
            'total_expenses':total_expenses,
            'net_saving':net_savings

        }

        return render(request,'finance/home.html',context=context)
    


class RegisterView(View):
    def get(self,request,*args,**kwargs):
        form=RegisterForm()
        return render(request,'finance/register.html',{'form':form})
    

    def post(self,request,*args,**kwargs):
        form=RegisterForm(request.POST) # to get form
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('login')
            
        return render(request, 'finance/register.html', {'form': form})
    


class GoalCreateView(LoginRequiredMixin,View):
    def get(self,request,*args,**kwargs):
        form=GoalsForm()
        return render(request,'finance/goal_form.html',{'form':form})
    

    def post(self,request,*args,**kwargs):
        form=GoalsForm(request.POST) # to get form
        if form.is_valid():
            Goal = form.save(commit=False)
            Goal.user = request.user  
            Goal.save()
            return redirect('goal_add')
            
        return render(request, 'finance/goal_form.html', {'form': form})
    

class GoalListView(LoginRequiredMixin,View):
    def get(self,request,*args,**kwargs):
        goal=Goal.objects.filter(user=request.user)
        return render(request,'finance/goal_list.html',{'goals':goal})
    








class TransactionCreateView(LoginRequiredMixin,View):
    def get(self,request,*args,**kwargs):
        form=TransactionForm()
        return render(request,'finance/transaction_form.html',{'form':form})
    

    def post(self,request,*args,**kwargs):
        form=TransactionForm(request.POST) # to get form
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user  
            transaction.save()
            return redirect('transaction_add')
            
        return render(request, 'finance/transaction_form.html', {'form': form})
    

class   TransactionListView(LoginRequiredMixin,View):
    def get(self,request,*args,**kwargs):
        transaction=Transaction.objects.filter(user=request.user)
        return render(request,'finance/transaction_list.html',{'transactions':transaction})
    