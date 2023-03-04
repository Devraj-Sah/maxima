# from asyncio.windows_events import NULL
import email
import datetime
# from turtle import back
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from PIL import Image
from django.contrib.auth.hashers import make_password

from root.models import *
from account.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import User,Group,Permission
from django.http import HttpResponseRedirect


def Login(request):
    if request.POST:
        # return HttpResponse("OK")
        email = request.POST['email']
        password =  request.POST['password']
        # return HttpResponse(password)
        user = authenticate(request=request,username=email, password=password)

        if user is not None:
            #return HttpResponse("loged in")
            return redirect('index_ecom')
            # A backend authenticated the credentials
        else:
             messages.error(request, "incorrect user or password")
             return render(request , 'main/login.html')
            # No backend authenticated the credentials
            # return render(request , 'admin/authentication/login.html')
    menus = Navigation.objects.filter(parent_page_id=0).order_by('position')
    blog = Blog.objects.filter(status=1)
    product = Products.objects.all()  
    data = {'page':"index",'menus':menus,'blog':blog,'product':product}
    return render(request , 'main/login.html',data)

def SignUp(request,id=None):
    if request.POST:
        if request.POST['password']!=request.POST['cpassword']:
            messages.error(request, "both password not match")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        data = {
            "first_name" : request.POST['first_name'],
            "username" : request.POST['last_name'],
            "email" :  request.POST['email'],
            "password" : make_password(request.POST['password']),
            "phone"    : request.POST['number'],
            "permanent_address" : request.POST['permanent_address'],            
        }       
        user,create = CustomUser.objects.update_or_create(id=id , defaults=data)#create customer account
        user.role = user.User
        user.save()
        login(request,user,backend='django.contrib.auth.backends.ModelBackend')

        return redirect('CheckOut')
    menus = Navigation.objects.filter(parent_page_id=0).order_by('position')
    blog = Blog.objects.filter(status=1)
    product = Products.objects.all()  
    data = {'page':"index",'menus':menus,'blog':blog,'product':product}
    return render(request , 'main/register.html',data)


@login_required(login_url=settings.LOGIN_URL)
def UserList(request):
    slug1 = "Users"
    create_link_name = reverse("UserCreate")
    all_data = User.objects.all()
    data = {'slug1':slug1,'create':True,'create_link_name':create_link_name, 'users':all_data}
    return render(request , "admin/users/user-list.html",data)

@login_required(login_url=settings.LOGIN_URL)
def UserCreate(request,id=None):
    create_link_name = reverse("UserCreate")
    if id==None:
        slug1 = "User-create" 
    else:
        slug1 = "User-update" 
    action = "UserStore"
    category = Navigation.objects.filter(page_type="group")
    #Fetching the data of particular ID
    get_data = None
    if id:
        # action = "ProductUpdate"
        get_data = User.objects.get(id=id)  
    data = {'slug1':slug1,'create':True,'create_link_name':create_link_name,'id_data':get_data, 'action':action,'category':category}
    return render(request, "admin/users/user-form.html",data)


@login_required(login_url=settings.LOGIN_URL)
def UserStore(request,id=None):
    if request.POST:
        data = {
            'first_name' : request.POST['first_name'],
            'last_name' : request.POST['last_name'],
            'user_name' : request.POST['user_name'],
            'password' : request.POST['password'],
            'email' : request.POST['email'],
            'image' : request.FILES['image'],
        }
        return HttpResponse(data)
        user = User.objects.update_or_create(id=id , defaults=data)
        return redirect(UserList)
    
@login_required(login_url=settings.LOGIN_URL)
def UserEdit(request):
    return HttpResponse("i am useredit")

@login_required(login_url=settings.LOGIN_URL)
def UserDelete(request):
    return HttpResponse("i am userdelete")

@login_required(login_url=settings.LOGIN_URL)
def RoleList(request):
    return HttpResponse("i am rolelist")

@login_required(login_url=settings.LOGIN_URL)
def RoleEdit(request):
    return HttpResponse("i am roleedit")

@login_required(login_url=settings.LOGIN_URL)
def RoleDelete(request):
    return HttpResponse("i am role delete")

@login_required(login_url=settings.LOGIN_URL)
def RoleStore(request):
    return HttpResponse("i am rolestore")

@login_required(login_url=settings.LOGIN_URL)
def PermissionList(request):
    return HttpResponse("i am permissionlist")

@login_required(login_url=settings.LOGIN_URL)
def PermissionEdit(request):
    return HttpResponse("i am permission edit")

@login_required(login_url=settings.LOGIN_URL)
def PermissionDelete(request):
    return HttpResponse("i am permission delete")

@login_required(login_url=settings.LOGIN_URL)
def PermissionStore(request):
    return HttpResponse("i am permission store")

@login_required(login_url=settings.LOGIN_URL)
def UserLogs(request):
    return HttpResponse("i am logs")

@login_required(login_url=settings.LOGIN_URL)
def UserLogs(request):
    return HttpResponse("i am logs")


def Logout(request):
    logout(request)
    return render(request , 'main/login.html')


