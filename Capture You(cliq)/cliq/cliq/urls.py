"""cliq URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from cliqapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home page"),
    path('cusregdisp/',views.cusregdisp,name="Customer Registration"),
    path('login/',views.login,name="login page"),
    path('viewpackage/',views.viewpackage,name="photographer view packages"),
    path('editpackage/',views.editpackage,name="photographer edit packages"),
    path('updatepackage/',views.updatepackage,name="photographer update packages"),
    path('adminviewusers/',views.adminviewusers,name="adminviewusers home"),
    path('associationhome/',views.associationhome,name="associationhome home"),

    path('adminhome/',views.adminpage,name="admin home"),
    path('customerhome/',views.customerhome,name="customerhome home"),
    path('photographerhome/',views.photographerhome,name="photographer home"),
    path('photographerprofile/',views.photographerprofile,name="photographerprofile home"),
    path('associationreg/',views.associationreg,name="association Registration"),

    path('customerregistration/',views.cusreg,name="Customer Registration"),
    path('photographerregistration/',views.photoreg,name="photographer Registration"),
    path('viewphotographers/',views.viewphotographers,name="view photographer"),
    path('viewassociation/',views.viewassociation,name="view viewassociation"),

    path('adminapprovepg/',views.adminapprovepg,name="approve photographer"),
    path('adminrejectpg/',views.adminrejectpg,name="Reject photographer"),
    path('adminapproveassoc/',views.adminapproveassoc,name="adminapproveassoc"),
    path('adminrejectassoc/',views.adminrejectassoc,name="adminrejectassoc "),
    path('addassoc/',views.addassoc,name="add addassoc"),
    path('photographeraddtoassoc/',views.photographeraddtoassoc,name="add photographeraddtoassoc"),

    path('addfeedback/',views.addfeedback,name="add feedback"),
    path('district/',views.district,name="add district"),
     path('pgaddpackage/',views.pgaddpackage,name="add pgaddpackage"),
     path('removepackage/',views.removepackage,name="remove pgaddpackage"),
        path('placelist/',views.placelist,name="view place"),
        path('placelist1/',views.placelist1,name="view placelist1"),

        path('photographerlist/',views.photographerlist,name="view photographerlist"),
        path('customerviewpackage/',views.customerviewpackage,name="view customerviewpackage"),

         path('customerviewphotographers/',views.customerviewphotographers,name="view place"),
    path('bookpg/',views.bookpg,name="Book"),
    path('morebooking/',views.morebooking,name="morebooking"),
    path('photographerupdatebookings/',views.photographerupdatebookings,name="photographerupdatebookings"),

    path('rate_now/',views.rate_now,name="rate_now"),
    path('award/',views.award,name="award"),
    path('adminviewallpg/',views.adminviewallpg,name="adminviewallpg"),

    path('phimage/',views.phimage,name="phimage"),
    path('phartimage/',views.phartimage,name="phartimage"),
    path('phgiftimage/',views.phgiftimage,name="phgiftimage"),
    path('photographerartgallery/',views.photographerartgallery,name="photographerartgallery"),


    path('phvideo/',views.phvideo,name="phvideo"),
    path('viewalbum/',views.viewalbum,name="viewalbum"),
    path('phspec/',views.phspec,name="phspec"),
    path('noti/',views.noti,name="noti"),
    path('Map/',views.Map,name="Map"),
    path('adminviewcomplaint/',views.adminviewcomplaint,name="adminviewcomplaint"),

    path('pgviewpayment/',views.pgviewpayment,name="pgviewpayment"),
    path('customeraddcomplaint/',views.customeraddcomplaint,name="customeraddcomplaint"),

    path('photographeraddcomplaint/',views.photographeraddcomplaint,name="photographeraddcomplaint"),
    path('viewvideo/',views.viewvideo,name="viewvideo"),
    path('viewvideolink/',views.viewvideolink,name="viewvideo"),
    path('photographerviewbookings/',views.photographerviewbookings,name="photographerviewbookings"),
    path('approvebooking/',views.approvebooking,name="approvebooking"),
    path('bookingprocessing/',views.bookingprocessing,name="bookingprocessing"),
    path('bookingcompleted/',views.bookingcompleted,name="bookingcompleted"),
    path('rejectbooking/',views.rejectbooking,name="rejectbooking"),
    path('viewnotification/',views.viewnotification,name="viewnotification"),
    path('viewrejectedbookings/',views.viewrejectedbookings,name="viewrejectedbookings"),
    path('assocmember/',views.assocmember,name="assocmember"),
    path('customerviewaward/',views.customerviewaward,name="customerviewaward"),
    path('photographerviewnotification/',views.photographerviewnotification,name="photographerviewnotification"),
    path('photographerviewassociation/',views.photographerviewassociation,name="photographerviewassociation"),
    path('payment1/', views.payment1, name='payment1'),

    path('requestmembership/', views.requestmembership, name='requestmembership'),
    path('payment2/', views.payment2, name='payment2'),
    path('payment3/', views.payment3, name='payment3'),
    path('payment4/', views.payment4, name='payment4'),
    path('payment5/', views.payment5, name='payment5'),
    path('goback/', views.goback, name='goback'),
    path('viewfeedback/', views.viewfeedback, name='viewfeedback'),
    path('contact/', views.contact, name='contact'),








  

    



]
