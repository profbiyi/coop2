# Create your models here.
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django import forms
# Create your models here.


class Profile(models.Model):
    '''Holds information about a user'''
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    salary = models.PositiveIntegerField()
    purse = models.PositiveIntegerField( null=True)
    number=models.IntegerField()
    role= models.BooleanField(default=False)
    refrence_no=models.IntegerField()
    picture=models.FileField(upload_to='media/user')
    age=models.IntegerField()

    def __unicode__(self):
        return self.role

class Loandb(models.Model):
    '''Holds all information about a loan'''
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.IntegerField()
    tenure=models.CharField(max_length=244)
    due_date = models.DateField(auto_now=True)
    guarantee=models.EmailField(null=True)
    gurantor_email=models.EmailField()
    monthly_installment = models.IntegerField()
    loan_request=models.CharField(max_length=200,null=True)

    def __unicode__(self):
        return 'Loan by {}'.format(self.user)
class Loanstatus(models.Model):
    loan=models.ForeignKey(Loandb,on_delete=models.CASCADE)
    admin_accept=models.CharField(max_length=300,null=True)
    grant=models.CharField(max_length=300,null=True)

