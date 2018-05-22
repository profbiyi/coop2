import json

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import  HttpResponseRedirect,HttpResponse
# Create your views here.
from django.urls import reverse
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView

from cooperative.models import Loandb, Profile, Loanstatus

from .forms import UserProfileForm, UserForm
from .forms import UserLoan
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm







def index(request):
    return render(request,'welcome.html')
    #return render(request,'login.html')
@login_required
def dashboard(request):
    if not request.user.is_authenticated:
        return render(request,'login.html')
    else:
     all_loans = Loandb.objects.all()
     return render(request,'dashboard.html',{'loan':all_loans})






class Register(CreateView):
    form_class = UserForm
    success_url = reverse_lazy("login")
    template_name = "signin.html"


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/dash/')
                    
    return render(request,'login.html')    



def Loan(request):
    if request.method =="POST":
        owner = request.user
        lon=Loandb.objects.filter(user=owner)
        amount=request.POST.get('amount')
        tenure = request.POST.get('tenure')
        install=request.POST.get('install')
        
        gua_email= request.POST.get('email')
        if gua_email==request.user.email:
            return render(request, 'info.html',
            {'message':'Your can not guarant yourself'})
        else:
            pass
        max_installment =((33/100)) * int(request.user.profile.salary)
        if int(install) >= max_installment:
            return render(request, 'info.html',
            {'message':'Your selected monthly installment exceeds the maximum allowed'})
        else:
            db=Loandb.objects.create(user=request.user,amount=amount,tenure=tenure,gurantor_email=gua_email,monthly_installment=install,loan_request='requested')
            db.save()
            return render(request, 'info.html',
            {'message':'Your have successfully applied for a Loan'})
            
            
    return redirect('/loa/')

def Loann(request):
    return render(request, 'loan.html')

def Noloan(request):
    if request.is_ajax:
        owner=request.user
        lon = Loandb.objects.filter(user=owner)
        for n in lon:
            print(n.loan_request)
        response = json.dumps({'req':n.loan_request})
    return HttpResponse(response, content_type="application/json")




def Guard(request):

    gurant=Loandb.objects.filter(gurantor_email=request.user.email)

    return  render(request,'gurantor.html',{
        'grant':gurant

    })

def Payment(request):
    return  render(request,'payment.html')

def Sales(request):
    return  render(request,'sales.html')
def dmin(request):
       all_loans = Loandb.objects.all()
       return render(request,'admin.html',{'loans':all_loans})


def Accept_Loan(request):
    if request.is_ajax:
        loan = request.POST.get('loan')
        post=Loandb.objects.get(id=loan)
        post.loanstatus_set.update(grant="accepted")
    return render(request, 'info.html',{'message':'You Accept'})
def Decline_Loan(request):
    if request.is_ajax:
        loan = request.POST.get('loan')
        post=Loandb.objects.get(id=loan)
        post.loanstatus_set.update(grant="Declined")
    return render(request, 'info.html',{'message':'You Decline'})

def Dim_accept(request):
    if request.is_ajax:
        loan = request.POST.get('id')
        post=Loandb.objects.get(id=loan)
        post.loanstatus_set.update(admin_accept="accepted")
    return render(request, 'info.html',{'message':'Admin Accept'})

def Dim_decline(request):
    if request.is_ajax:
        loan = request.POST.get('id')
        post=Loandb.objects.get(id=loan)
        post.loanstatus_set.update(admin_accept="decline")
    return render(request, 'info.html',{'message':'Admin Decline'})
        






