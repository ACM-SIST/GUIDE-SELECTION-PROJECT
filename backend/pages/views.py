
import string
from random import choice
from django.core.mail import send_mail
from guide_project.settings import EMAIL_HOST_USER
from django.contrib.auth.models import User
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
        emp_id = request.POST['emp_id']
        serial_no = request.POST['serial_no']
        designation = request.POST['designation']
        domain_1 = request.POST['domain_1']
        domain_2 = request.POST['domain_2']
        domain_3 = request.POST['domain_3']
        email = request.POST['email']
        # experience = request.POST['experience']
        myImage = request.FILES['myImage']

        name = first_name + ' ' + last_name

        serial_no = int(serial_no)

        if serial_no >= 1 and serial_no <= 52:
            vacancy = 7
        elif serial_no >= 53 and serial_no <= 79:
            vacancy = 4
        else:
            vacancy = 3

        if Guide.objects.filter(serial_no=serial_no).exists():
            messages.error(
                request, 'This serial number already exists. Please enter your own serial number')
            return redirect('guides')
        else:
            guide = Guide(serial_no=serial_no, emp_id=emp_id, designation=designation, name=name, domain_1=domain_1, domain_2=domain_2,
                          domain_3=domain_3, email=email, myImage=myImage, vacancy=vacancy)

            guide.save()
        return render(request, 'adminregister/submitted.html')
    else:

        return render(request, 'aform.html')


def submitted(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        # user_name = request.POST['Username']
        email = request.POST['email']
        password = request.POST['password']
        ConfirmPassword = request.POST['password1']

        if password == ConfirmPassword:
            if User.objects.filter(username=email).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=email, email=email, password=password)
                # opt verify under if cond.
            if email:
                chars = string.digits
                random = ''.join(choice(chars) for i in range(4))
                random_otp = int(random)
                user_otp = random_otp
                send_mail('RANDOM OTP', 'The OTP is: '+random, EMAIL_HOST_USER,
                [email, ], fail_silently=False,)
                return render(request, 'Register/verify.html')

                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password not matching')
            return redirect('register')
    else:
        return render(request, 'Register/register.html')


def login(request):
    if request.method == 'POST':
        user_name = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username=user_name, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('project-details')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'Login/login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


def project_details(request):

    if request.method == 'POST':

        project_details.project_name = request.POST['project_name']
        project_details.project_domain = request.POST['project_domain']
        project_details.project_description = request.POST['project_description']
        project_details.no_of_members = request.POST['no_of_members']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        project_details.reg_no_1 = request.POST['reg_no_1']
        project_details.student_1_email = request.POST['student_1_email']
        project_details.student_1_no = request.POST['student_1_no']

        project_details.name = first_name + ' ' + last_name

        if project_details.no_of_members == '2':
            first_name_2 = request.POST['first_name']
            last_name_2 = request.POST['last_name']
            project_details.reg_no_2 = request.POST['reg_no_1']
            project_details.student_2_email = request.POST['student_1_email']
            project_details.student_2_no = request.POST['student_1_no']

            project_details.name_2 = first_name_2 + ' ' + last_name_2

        return redirect('select-guide')
    else:
        return render(request, 'project_form/project_form.html')


def select_guide(request):

    guides = Guide.objects.order_by('serial_no')
    if request.method == 'POST':

        return redirect('guide-selected')

    # print(type(guides.id))

    context = {
        'guides': guides,
    }

    return render(request, 'GuideList/guide.html', context)


def guide_selected(request, id):

    guides = Guide.objects.filter(serial_no=id)

    context = {
        'guides': guides,
    }

    return render(request, 'submitted.html')


'''def export_team_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'

    writer = csv.writer(response)
    writer.writerow(['Username', 'First name', 'Last name', 'Email address'])

    users = User.objects.all().values_list(
        'username', 'first_name', 'last_name', 'email')
    for user in users:
        writer.writerow(user)

    return response'''

def verify_single(request):
    if request.method == 'POST':
        opt = request.POST['otp']
        user_otp = int(opt)
        if mail_single.user_otp == user_otp:
            send_mail(
                'THANK YOU',
                'Your Email is verified ',
                EMAIL_HOST_USER,
                [mail_single.user_email],
                fail_silently=False,
            )
            return redirect('main')
        else:
            return redirect('register')
    else:
        return redirect('register')
