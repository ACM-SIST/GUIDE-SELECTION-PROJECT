
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from pages.models import Guide

# Create your views here.


def home(request):
    return render(request, 'Home/home.html')


def guides(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        domain_1 = request.POST['domain_1']
        domain_2 = request.POST['domain_2']
        domain_3 = request.POST['domain_3']
        email = request.POST['email']
        experience = request.POST['experience']
        myImage = request.FILES['myImage']

        name = first_name + ' ' + last_name

        guide = Guide(name=name, domain_1=domain_1, domain_2=domain_2,
                      domain_3=domain_3, email=email, experience=experience, myImage=myImage)

        guide.save()
        return render(request, 'adminregister/submitted.html')
    else:

        return render(request, 'aform.html')


def submitted(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        user_name = request.POST['Username']
        email = request.POST['Email']
        password = request.POST['Password']
        ConfirmPassword = request.POST['Password1']

        if password == ConfirmPassword:
            if User.objects.filter(username=user_name).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=user_name, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password not matching')
            return redirect('register')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        user_name = request.POST['Username']
        password = request.POST['Password']

        user = auth.authenticate(username=user_name, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('form')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

def form(request):
    return render(request,'form.html')


def project_details(request):

    if request.method == 'POST':

        project_name = request.POST['project_name']
        project_domain = request.POST['project_domain']
        project_description = request.POST['project_description']
        no_of_members = request.POST['no_of_members']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        reg_no_1 = request.POST['reg_no_1']
        student_1_email = request.POST['student_1_email']
        student_1_no = request.POST['student_1_no']

        if no_of_members == '2':
            first_name_2 = request.POST['first_name']
            last_name_2 = request.POST['last_name']
            reg_no_2 = request.POST['reg_no_1']
            student_2_email = request.POST['student_1_email']
            student_2_no = request.POST['student_1_no']

        return redirect('select-guide')
    else:
        return render(request, 'project_form/project_form.html')


def select_guide(request):
    return render(request, 'GuideList/guide.html')
