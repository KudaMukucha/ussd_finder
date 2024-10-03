from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate,get_user_model
from django.contrib import messages

# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user is not None and user.is_active:
            login(request,user)
            return redirect('codes:codes-list')
        else:
            messages.warning(request,'Oops,something went wrong. Please try again')
            return redirect('accounts:login')
    return render(request,'accounts/login.html')

def logout_user(request):
    logout(request)
    return redirect('accounts:login')
