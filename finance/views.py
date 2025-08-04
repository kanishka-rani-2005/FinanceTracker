from django.shortcuts import render,redirect
from django.http  import HttpRequest
from django.views import View
from .forms import RegisterForm
from django.contrib.auth import login


def Home(request):
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