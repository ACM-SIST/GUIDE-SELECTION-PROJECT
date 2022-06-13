
import csv
import string
from random import choice
from django.core.mail import send_mail
from guide_project.settings import EMAIL_HOST_USER
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.http import HttpResponse
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
        experience = request.POST['experience']
        myImage = request.FILES['myImage']

        name = first_name + ' ' + last_name

        serial_no = int(serial_no)

        if serial_no >= 1 and serial_no <= 3:
            vacancy = 7
        elif serial_no >= 4 and serial_no <= 6:
            vacancy = 2

        guide = Guide(serial_no=serial_no, emp_id=emp_id, designation=designation, name=name, domain_1=domain_1, domain_2=domain_2,
                      domain_3=domain_3, email=email, experience=experience, myImage=myImage, vacancy=vacancy)

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


def mail_single(request):
    if request.method == 'POST':
        email = request.POST['mail']
        mail_single.user_email = email
        chars = string.digits
        random = ''.join(choice(chars) for i in range(4))
        random_otp = int(random)
        mail_single.user_otp = random_otp
        send_mail('RANDOM OTP', 'The OTP is: '+random, EMAIL_HOST_USER,
                  [mail_single.user_email, ], fail_silently=False,)
        return render(request, 'verify.html', {'o': mail_single.user_otp})
        # return render(request,'verify.html')
    else:
        return render(request, 'mail.html')


def mail_two(request):
    if request.method == 'POST':
        email = request.POST['mail']
        email1 = request.POST.get('maill', False)
        mail_two.user_email = email
        mail_two.user_email1 = email1
        chars = string.digits
        random = ''.join(choice(chars) for i in range(4))
        random_otp = int(random)
        mail_two.user_otp = random_otp
        otp = str(random)
        mail_two.user_otp1 = otp[:2]
        mail_two.user_otp2 = otp[2:]
        m = [mail_two.user_otp1, mail_two.user_otp2]
        send_mail(
            'RANDOM OTP',
            'The OTP is: ' + mail_two.user_otp1,
            EMAIL_HOST_USER,
            [mail_two.user_email, ],
            fail_silently=False,
        )

        send_mail(
            'RANDOM OTP',
            'The OTP is: ' + mail_two.user_otp2,
            EMAIL_HOST_USER,
            [mail_two.user_email1, ],
            fail_silently=False,
        )

        return render(request, 'verify1.html', {'e': m})
    else:
        return render(request, 'mail1.html')


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
            return render(request, 'mail.html')
    else:
        return render(request, 'mail.html')


def verify_two(request):
    if request.method == 'POST':
        otp = request.POST['otp']
        otp1 = request.POST.get('otp1', False)
        user_otp = int(otp)
        user_otp1 = int(otp1)
        if int(mail_two.user_otp1) == user_otp and int(mail_two.user_otp2) == user_otp1:
            send_mail('THANK YOU', 'Your Email is verified ', EMAIL_HOST_USER, [
                      mail_two.user_email], fail_silently=False,)
            send_mail('THANK YOU', 'Your Email is verified ', EMAIL_HOST_USER, [
                      mail_two.user_email1], fail_silently=False,)
            return redirect('main')
        else:
            return render(request, 'mail1.html')
    else:
        return render(request, 'mail1.html')
