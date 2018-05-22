from django import  forms
from django.contrib.auth.models import  User
from .models import Profile, Loandb
from django.contrib.auth.forms import UserCreationForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=('username','email','first_name','last_name','password',)
class UserLogin(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=('email','password',)

class UserProfileForm(forms.ModelForm):
      class Meta():
          model=Profile
          fields=('salary','number','refrence_no','picture','age',)


class UserLoan(forms.ModelForm):
    class Meta():
        model = Loandb
        fields = ('amount','tenure','monthly_installment','gurantor_email')