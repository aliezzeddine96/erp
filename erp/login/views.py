from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def login_view(request):
    # form = LoginForm(request.POST or None)
    # if form.is_valid():
    #     username = form.cleaned_data.get('username')
    #     password = form.cleaned_data.get('password')
    #     user = authenticate(request, username=username, password=password)
    #     if user is None:
    #         return render(request, 'login/login.html', {'error_message': '*Invalid username or password '})
    #     else:
    #         login(request, user)
    #         return redirect('/dashboard/')
    # return render(request, 'login/login.html', {})
    if request.POST:
        response = request.POST
        username = response.get('username')
        password = response.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            return render(request, 'login/login.html', {'error_message': '*Invalid username or password '})
        else:
            login(request, user)
            return redirect('/dashboard/')
    else:
        if request.user.is_authenticated:
            return redirect('/dashboard/')
        else:
            return render(request, 'login/login.html', {'error_message': ''})


def logout_view(request):
    logout(request)
    return redirect("/login/")
