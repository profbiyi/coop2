"""coop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path,re_path
from cooperative import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import logout

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('^$',views.index,name='index'),
    path('dash/',views.dashboard,name='dash'),
    path('login/',views.login_user,name='login'),
    #path('log/',views.logi,name='log'),
    path('logout/', logout, { 'template_name': 'logged_out.html',}, name='logout' ),
    #path('logout/',auth_views.LogoutView.as_view(), name="logout"),
    path('register/', views.Register.as_view(), name='register'),
    #path('profile/', views.Profile.as_view(), name='profile'),
    path('load/', views.Loan, name='loan'),
    path('loa/', views.Loann, name='loann'),
    path('noloan/', views.Noloan, name='no'),
    path('guarantor/', views.Guard, name='guard'),
    path('payment/', views.Payment, name='payment'),
    path('sales/', views.Sales, name='sales'),
    path('accept/', views.Accept_Loan, name='accept'),
    path('decline/', views.Decline_Loan, name='decline'),
    path('dim/', views.dmin, name='dmin'),
    path('admin_accept/', views.Dim_accept, name='admin_accept'),
    path('admin_decline/', views.Dim_decline, name='admin_decline'),


   # path('guarantor_decline/', views.Decline_Loan, name='decline'),

#

]
if settings.DEBUG:
   urlpatterns +=staticfiles_urlpatterns(settings.STATIC_ROOT)
   urlpatterns +=staticfiles_urlpatterns(settings.MEDIA_ROOT)
