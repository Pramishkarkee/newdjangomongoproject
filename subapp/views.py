from django.shortcuts import render,redirect
from .import models
from django.http import HttpResponse

# Create your views here.
def login(request):
    return render(request,'login.html')
def index(request):
    if request.method == 'POST':
        username=request.POST.get('username',False)
        password=request.POST.get('password',False)
        print("*********",username,"**********")
        print("*********",password,"**********")
        return render(request,'index.html')
def register(request):
    return render(request,'register.html')
def submit_form(request):
    if request.method=="POST":
        username=request.POST.get('username',False)
        password=request.POST.get('password',False)
        models.register_form(username,password)
        return HttpResponse("success to save in db")
    