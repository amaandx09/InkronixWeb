from django.shortcuts import render,HttpResponseRedirect, HttpResponse
from django.views import View
from django.contrib import messages
from .models import *
# Create your views here.

class Home(View):
    
    def get(self,request):
        
        return render(request,'home.html',{'home':True})

    def post(self,request):
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        details = request.POST['details']
        Project(name=name,email=email,phone=phone,details=details).save()
        messages.success(request,f"Hello, {name} Thanks for contacting us! We will reach you soon!!")
        return HttpResponseRedirect('/')
    
class Team(View):
    
    def get(self,request):
        
        return render(request,'team.html',{'team':True})

    def post(self,request):
        
        
        return HttpResponseRedirect('/')
    
class WhatWeDo(View):
    
    def get(self,request):
        
        return render(request,'we_do.html',{'we_do':True})

    def post(self,request):
        
        
        return HttpResponseRedirect('/')
    
class AdminLogin(View):
    
    def get(self,request):
        
        return HttpResponseRedirect('/admin/')

    


    