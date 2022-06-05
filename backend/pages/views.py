
from django.shortcuts import redirect, render

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
    return render(request, 'Register/register.html')


def login(request):
    if request.method == 'POST':
        return redirect('project-details')
    return render(request, 'Login/login.html')


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
