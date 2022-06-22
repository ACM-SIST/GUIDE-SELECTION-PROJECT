
import string
from random import choice
from django.core.mail import send_mail
from guide_project.settings import EMAIL_HOST_USER
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from pages.models import Guide, Team

# Create your views here.


def home(request):
    return render(request, 'Home/home.html')


def no_of_stud(request):
    return render(request, 'no_of_stud/no_of_stud.html')


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
        email = request.POST['email']
        password = request.POST['password']
        ConfirmPassword = request.POST['password1']

        if password == ConfirmPassword:
            if User.objects.filter(username=email).exists():
                messages.error(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email Taken')
                return redirect('register')
            else:

                user = User.objects.create_user(
                    username=email, email=email, password=password)

                # opt verify under if cond.
                #
                user.save()

                return redirect('login')
        else:
            messages.error(request, 'Password not matching')
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
            team = Team.objects.filter(teamID=user.username).exists()
            if team is not None:
                if team.no_of_members == 2:
                    return redirect('project-details-2')
            return redirect('project-details-1')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'Login/login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


def project_details_1(request):

    if request.method == 'POST':

        project_name = request.POST['project_name']
        project_domain = request.POST['project_domain']
        project_description = request.POST['project_description']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        reg_no_1 = request.POST['reg_no_1']
        student_1_email = request.POST['student_1_email']
        student_1_no = request.POST['student_1_no']

        student_1_name = first_name + ' ' + last_name

        curr_user = request.user

        user = User.objects.get(username=curr_user.username)
        print("TYPE OF user.id: ", type(user.id))

        # CSE-<team_id_num> for eg: CSE-007, CSE-008....
        new_username = "CSE-%03d" % user.id
        team = Team.objects.create(teamID=curr_user.username, project_name=project_name, project_domain=project_domain, project_description=project_description,
                                   no_of_members='1', reg_no_1=reg_no_1, student_1_name=student_1_name, student_1_email=student_1_email, student_1_no=student_1_no)

        print('NAME IS: ', team.project_name)
        print('TEAMID IS: ', team.teamID)
        user.username = new_username

        user.save()

        return redirect('select-guide')
    else:
        return render(request, '1_project_form/1_project_form.html')


def project_details_2(request):

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

        student_1_name = first_name + ' ' + last_name

        first_name_2 = request.POST['first_name']
        last_name_2 = request.POST['last_name']
        reg_no_2 = request.POST['reg_no_1']
        student_2_email = request.POST['student_1_email']
        student_2_no = request.POST['student_1_no']

        student_2_name = first_name_2 + ' ' + last_name_2

        curr_user = request.user

        user = User.objects.get(username=curr_user.username)
        print("TYPE OF user.id: ", type(user.id))

        # CSE-<team_id_num> for eg: CSE-007, CSE-008....
        team = Team.objects.create(teamID=curr_user.username, project_name=project_name, project_domain=project_domain, project_description=project_description,
                                   no_of_members='1', reg_no_1=reg_no_1, student_1_name=student_1_name, student_1_email=student_1_email, student_1_no=student_1_no, reg_no_2=reg_no_2, student_2_name=student_2_name, student_2_email=student_2_email, student_2_no=student_2_no)
        new_username = "CSE-%03d" % user.id
        print('NAME IS: ', team.project_name)
        print('TEAMID IS: ', team.project_name)
        user.username = new_username

        user.save()

        return redirect('select-guide')
    else:
        return render(request, '2_project_form/2_project_form.html')


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

    guide = Guide.objects.filter(serial_no=id)

    # you can get teamID from username as both are same.
    team = get_object_or_404(Team, teamID='CSE-001')

    # print('TEAM IS: ', queryset_list.filter(teamID__iexact='CNN'))
    print('TEAM IS: ', team)
    # print('TEAM IS: ', queryset_list.project_name)
    print('GUIDE IS: ', guide)

    context = {
        'guide': guide,
        'team': team,
    }

    return render(request, 'confirmation_2/confirmation.html', context)


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
