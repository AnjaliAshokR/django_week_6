from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.views.decorators.cache import cache_control
from .forms import Accountform
from django.db.models import Q


# Create your views here.
# login view function for user
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login(request):
    if 'user' in request.session:
        return redirect('home')

    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            request.session['user'] = username
            auth.login(request,user)
            response = redirect('home')
            response.set_cookie('username',username)
            response.set_cookie('logged_in', True)
            return response
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('credentials:login')
    else:
        return render(request, 'login.html')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def admin_login(request):
    if 'super' in request.session:
        return redirect('credentials:admin')
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user = auth.authenticate(username=username,password=password)
        s = user.is_superuser
        if s:
            request.session['super'] = username
            request.session['user']=username
            auth.login(request, user)
            response = redirect('credentials:admin')
            response.set_cookie('username', username)
            response.set_cookie('logged_in', True)
            return response
        else:
            return redirect('welcome_page')
    else:
        return render(request, 'adminlogin.html')

#  view function for registration
def register(request):
    if request.method =='POST':
        first_name=request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken!')
                return redirect('credentials:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken!')
                return redirect('credentials:register')
            else:
                user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,password=password,email=email)
                user.save();
                return redirect('credentials:login')
        else:
            messages.info(request,"Password doesn't match!")
            return redirect('credentials:register')
    else:
        return render(request,'register.html')

#  view function for admin page
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def admin(request):
    if 'super' in request.session:
        users = User.objects.all().order_by('id')
        return render(request,'admin.html',{'users':users})
    return redirect('credentials:login')
#  view function for logging out
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout(request):
    response = redirect('credentials:login')
    if 'user' in request.session:
        response.delete_cookie('username')
        response.delete_cookie('logged_in')
        request.session.flush()
        auth.logout(request)
    return response


#  view function for user details updation
def update(request,id):
    if 'super' in request.session:
        add_user = User.objects.get(id=id)
        form = Accountform(request.POST or None, instance=add_user)
        if form.is_valid():
            form.save();
            return redirect('credentials:admin')
        return render(request,'update.html', {'form':form, 'add_user':add_user})
    return redirect('welcome_page')

#  view function for deleting a user
def delete(request,id):
    if 'super' in request.session:
        user = User.objects.get(id=id)
        if request.method=='POST':
            user.delete()
            return redirect('credentials:admin')
        return render(request,'delete.html')
    return redirect('welcome_page')

#  view function for adding a user from the admin page
def add(request):
    if 'super' in request.session:
        if request.method =='POST':
            username=request.POST.get('username', '')
            first_name = request.POST.get('first_name', '')
            last_name = request.POST.get('last_name', '')
            password=request.POST.get('password','')
            email=request.POST.get('email','')
            confirm_password=request.POST.get('confirm_password')
            if password==confirm_password:
                add_user=User.objects.create_user(username=username,first_name=first_name, last_name=last_name,email=email,password=password)
                add_user.save();
                return redirect('credentials:admin')
        return render(request, 'add.html')
    return redirect('welcome_page')

#  view function for searching user details
def SearchResult(request):
    if 'super' in request.session:
        users=None
        query=None
        if 'q' in request.GET:
            query=request.GET.get('q')
            users=User.objects.all().filter(Q(first_name__contains=query) | Q(last_name__contains=query) | Q(email__contains=query) | Q(username__contains=query))
            return render(request,'search.html', {'query': query, 'users': users})
    return redirect('welcome_page')