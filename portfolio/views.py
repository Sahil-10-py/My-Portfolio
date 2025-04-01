from django.shortcuts import render,redirect
from .models import Portfolio
from django.contrib import messages

def portfolio(request):
    if request.method == "POST":
        # Fetch form data
        name = request.POST.get('name')
        course = request.POST.get('course')
        biography = request.POST.get('biography')
        dob = request.POST.get('dob')
        gmail = request.POST.get('gmail')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        projects = request.POST.get('projects')
        
        # Create portfolio object
        Portfolio.objects.create(
            name=name,
            course=course,
            biography=biography,
            dob=dob,
            gmail=gmail,
            phone=phone,
            city=city,
            projects=projects
        )
        
        portfolio_list = Portfolio.objects.all()
        return render(request, "home.html", {"a": portfolio_list})
    
    else:
        return render(request, "form.html")


def home_view(request):
    portfolio_list = Portfolio.objects.all()
    return render(request, "home.html", {"a": portfolio_list})

def biography(request):
    portfolio_list = Portfolio.objects.all()
    return render(request, 'biography.html',{"a": portfolio_list})

def projects_view(request):
    portfolio_list = Portfolio.objects.all()
    return render(request, 'projects.html',{"a": portfolio_list})

def p_info(request):
    portfolio_list = Portfolio.objects.all() 
    return render(request, 'p_info.html',{"a": portfolio_list})
