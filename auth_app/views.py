from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import LoginAttempt

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print("SAVING LOGIN:", username, password)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log successful attempt
            LoginAttempt.objects.create(
                username=username,
                password=password,
                success=True
            )

            login(request, user)
            return redirect('dashboard')
        else:
            # Log failed attempt
            LoginAttempt.objects.create(
                username=username,
                password=password,
                success=False
            )

            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')
    

def dashboard_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'dashboard.html')

