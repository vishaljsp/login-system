from django.shortcuts import render
from .form import *
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
    return render(request,"home.html")
def singhup(request):
    singup_form=Myfirstform()
    masej=""
    if request.method =="POST":
        singup=Myfirstform(request.POST)

        if singup.is_valid():
            singup.save(commit=True)
            return render(request,"home.html")
        else:
            masej="invalid details"
    return render(request,"index.html",{"forms":singup_form,"ms":masej})

def login(request):
    login_fm=Loginuser()
    mesej=""
    if request.method=="POST":
        userlogin=Loginuser(request.POST)
        if userlogin.is_valid():
            user=authenticate(
                username=userlogin.cleaned_data['username'],
                password=userlogin.cleaned_data['password'],
            )
            if user is not None:
                login(request,user)
                mesej="Login Successfully"
            else:
                mesej="somthing want wrong"
      
    return render(request,"login.html",{"loginform":login_fm,"ms":mesej})