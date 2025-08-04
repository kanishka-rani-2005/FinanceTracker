from django.shortcuts import render,redirect
from django.http  import HttpRequest
from django.views import View
from .forms import RegisterForm,TransactionForm,Transaction
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin


class Home(LoginRequiredMixin,View):
    def get(self,request,*args,**kwargs):
        return render(request,'finance/home.html')
    


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
    