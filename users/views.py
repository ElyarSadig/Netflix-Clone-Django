from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import User
from .forms import MyUserForm
from django.contrib import messages


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('profile-list')

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)

        except:
            messages.error(request, 'User does not exist!')

        user = authenticate(request, email=email, password=password)

        if user:
            login(request, user)
            return redirect('profile-list')

        else:
            messages.error(request, 'Username With This Password does not exist')

    return render(request, 'users/login.html')


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = MyUserForm()
    if request.method == 'POST':

        form = MyUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')

    context = {'form': form}
    return render(request, 'users/signup.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')
