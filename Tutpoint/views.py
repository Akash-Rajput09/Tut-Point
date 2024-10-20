from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from courses.models import Course

def home(request):
    top_enrolled_courses = Course.objects.order_by('-enrollment_count')[:4]
    top_recent_courses = Course.objects.order_by('-created_at')[:4]
    return render(request, 'index.html',{
        'top_enrolled_courses': top_enrolled_courses,
        'top_recent_courses': top_recent_courses,
    })

def signup(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['change-password']
        name = request.POST['name']

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return render(request, 'signup.html')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'signup.html')

        # Create user
        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = name
        
        login(request, user)
        messages.success(request, 'Signup successful! Welcome.')
        return redirect('home')

    return render(request, 'signup.html')

def login_view(request):
    next_page = request.GET.get('next', 'home')
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                login(request, user)
                return redirect(next_page)
            else:
                messages.error(request, 'Invalid email or password.')
        except User.DoesNotExist:
            messages.error(request, 'Invalid email or password.')
    
    return render(request, 'login.html')

@login_required
def teach(request):
    user = request.user
    courses = Course.objects.filter(author=user)
     
    return render(request, 'teach.html',{'courses':courses})

@login_required
def user_profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})