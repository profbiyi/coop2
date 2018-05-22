from django.contrib import admin
from .models import Profile, Loandb,Loanstatus

# Register your models here.
admin.site.register(Profile)
admin.site.register(Loanstatus)
class LoanAdmin(admin.ModelAdmin):
  list_display = ['id','user','amount']



admin.site.register(Loandb,LoanAdmin)

