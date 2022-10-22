
from random import randrange
from django.core.mail import send_mail
from django.http import HttpResponse
from guide_project.settings import EMAIL_HOST_USER
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from pages.models import Guide, Team, Otp, Otp_Two, Temp_Team


# Create your views here.


def home(request):
    # if request.method == 'POST':
    #     return render(request, 'Register/register.html')
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
    # auth.logout(request)
    return render(request, 'submitted.html')


def register(request):
    print('INSIDE REGISTER FUNCTION')
    print('REQUEST METHOD: ', request.method)
    if request.method == 'POST':
        print('INSIDE POST IF: ')
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        ConfirmPassword = request.POST['password1']
        temp = email.split('@')
        print("DOMAIN IS: ", temp)
        if temp[1] == 'gmail.com' or temp[1] == 'yahoo.in' or temp[1] == 'hotmail.com':

            if password == ConfirmPassword:
                special_characters = "[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]"
                if len(password) < 8:
                    messages.error(
                        request, 'Password length must be atleast 8 character.')
                    return redirect('register')
                if not any(char.isdigit() for char in password):
                    messages.error(
                        request, 'Password must contain at least 1 digit.')
                    return redirect('register')
                if not any(char.isalpha() for char in password):
                    messages.error(
                        request, 'Password must contain at least 1 letter and must be alpha-numeric.')
                    return redirect('register')
                if not any(char in special_characters for char in password):
                    messages.error(
                        request, 'Password must contain at least 1 special character')
                    return redirect('register')
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email Taken')
                    return redirect('register')
                elif Team.objects.filter(student_1_email=email).exists():
                    messages.error(request, 'Email Taken in another team')
                    return redirect('register')
                elif Team.objects.filter(student_2_email=email).exists():
                    messages.error(request, 'Email Taken in another team')
                    return redirect('register')
                else:

                    user = User.objects.create_user(
                        first_name=first_name, last_name=last_name, username=email, email=email, password=password
                    )

                    user.save()
                    auth.login(request, user)

                    return redirect('verify')
            messages.error(request, 'Password not matching')
            return render(request, 'Register/register.html')
        else:
            messages.error(
                request, 'Enter a valid email with @gmail.com, @yahoo.in, @hotmail.com')
            return redirect('register')

    else:
        print("INSIDE ELSE")
        return render(request, 'Register/register.html')


def verify(request):
    user = request.user
    t = Otp.objects.filter(user_email=user.email)

    if request.method == 'POST':
        otp = request.POST['otp']
        g_otp = Otp.objects.filter(user_email=user.email).get()

        if otp == g_otp.otp:
            auth.logout(request)
            t.delete()
            messages.success(request, 'Account Verified! You can login.')

            return render(request, 'Login/login.html')
        else:
            auth.logout(request)
            user.delete()
            t.delete()
            messages.error(request, 'Invalid OTP. Please try again.')
            return render(request, 'Register/register.html')
    else:

        no = randrange(1000, 9999)
        print("OTP IS: ", no)
        if Otp.objects.filter(user_email=user.email).exists():
            t = Otp.objects.filter(user_email=user.email)
            t.delete()
            print("OTP DELETED AND SENT AGAIN")
        email = Otp.objects.create(user_email=user.email, otp=no)
        email.save()
        send_mail(
            'YOUR OTP for verification',
            'Your OTP is: {}'.format(no),
            EMAIL_HOST_USER,
            [user.email, ],
            fail_silently=False,
        )

        return render(request, 'Register/verify.html')


def mail1(request):
    user = request.user
    if request.method == 'POST':
        # email_1 = request.POST['email_1']
        email_2 = request.POST['email_2']

        no = randrange(1000, 9999)
        print("2nd MEMBER OTP IS: ", no)
        if Otp_Two.objects.filter(user_email=email_2).exists():
            t = Otp_Two.objects.filter(user_email=email_2)
            t.delete()
            print("OTP DELETED AND SENT AGAIN")
        if User.objects.filter(email=email_2).exists():
            messages.error(
                request, 'The mail id already registered!')
            return redirect('mail1')
        elif Team.objects.filter(student_2_email=email_2).exists():
            messages.error(
                request, 'The Second mail id already exists with another team!')
            return redirect('mail1')
        elif Team.objects.filter(student_1_email=email_2).exists():
            messages.error(
                request, 'The Second mail id already exists with another team!')
            return redirect('mail1')
        email = Otp_Two.objects.create(
            user_email=email_2, temp_email=request.user.email, otp=no)
        email.save()
        send_mail(
            'YOUR OTP for verification',
            'Your OTP is: {}'.format(no),
            EMAIL_HOST_USER,
            [email_2, ],
            fail_silently=False,
        )

        return redirect('verify1')
    else:
        user = request.user
        context = {
            'user': user,
        }
        return render(request, 'Register/mail1.html', context)


def verify1(request):
    if request.method == 'POST':
        otp = request.POST['otp']
        if Otp_Two.objects.filter(temp_email=request.user.email).exists():
            g_otp = Otp_Two.objects.filter(temp_email=request.user.email).get()

        if otp == g_otp.otp:
            return redirect('project-details-2')
    else:
        return render(request, 'Register/verify1.html')


def login(request):
    if request.method == 'POST':
        user_name = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username=user_name, password=password)
        if user is not None:
            auth.login(request, user)

            user = request.user

            if Temp_Team.objects.filter(student_1_email=user.email).exists():
                team = Temp_Team.objects.filter(
                    student_1_email=user.email).get()
<<<<<<< HEAD
<<<<<<< HEAD
                if Guide.objects.filter(serial_no=team.guide).exists():
                    guide_inst = Guide.objects.filter(
                        serial_no=team.guide).get()
                    context = {
                        'team': team,
                        'user': user,
                        'guide': guide_inst,
                        'id': guide_inst.serial_no
                    }
                else:
                    team.delete()
                    return render(request, 'no_of_stud/no_of_stud.html')
=======
                # guide_inst = Guide.objects.filter(
                #     serial_no=team.guide.serial_no).get()
                context = {
                    'team': team,
                    'user': user,
                    # 'guide': guide_inst,
                    # 'id': guide_inst.serial_no
                }

>>>>>>> 4abf7792c60add63574d1bcddfe7369d7089ab91
                if team.no_of_members == '2':
                    return render(request, 'temp_team_2/temp_team_2.html', context)
=======
                g_obj = team.guide
                email_2 = Otp_Two.objects.filter(temp_email=user.email).get()
                print('TYPE OF g_obj: ', type(g_obj))
                if g_obj is None:
                    print('INSIDE NONE IF')
                    context = {
                        'email': email_2
                    }

                    if team.no_of_members == '2':
                        return render(request, '2_project_form/2_project_form.html', context)
                    else:
                        return render(request, '1_project_form`/1_project_form.html')
>>>>>>> 224e5c37fe1b84ffe7f96e20cbde234c26ae5766
                else:
                    print('INSIDE NONE ELSE')
                    context = {
                        'team': team,
                        'user': user,
                        # 'guide': guide_inst,
                        # 'id': guide_inst.serial_no
                    }

                    if team.no_of_members == '2':
                        return render(request, 'temp_team_2/temp_team_2.html', context)
                    else:
                        return render(request, 'temp_team_1/temp_team_1.html', context)

            if Team.objects.filter(teamID=user.username).exists():
                auth.logout(request)
                messages.info(
                    request, 'Your team is already registered. Please contact project co-ordinator!')
                return render(request, 'Login/login.html')
            return render(request, 'no_of_stud/no_of_stud.html')
        else:
            messages.error(request, 'Invalid Credentials')
            return render(request, 'Login/login.html')
    else:
        return render(request, 'Login/login.html')


def logout(request):
    auth.logout(request)
    messages.success(request, 'You are successfully logged Out and can login!')
    return render(request, 'Login/login.html')


def project_details_1(request):
    guides = Guide.objects.order_by('serial_no')
    curr_user = request.user
    if Temp_Team.objects.filter(student_1_email=curr_user.email).exists():
        obj = Temp_Team.objects.filter(student_1_email=curr_user.email).get()
        obj.delete()
    if Team.objects.filter(teamID=curr_user.username).exists():
        is_team = Team.objects.filter(teamID=curr_user.username).get()
        guide_inst = Guide.objects.filter(serial_no=is_team.guide)
        is_team.delete()
        is_user = User.objects.filter(username=is_team.teamID)
        is_user.delete()
        messages.info(
            request, 'Your team is removed please to the process again!!')
        return render(request, 'Login/login.html')

    if request.method == 'POST':

        project_name = request.POST['project_name']
        project_domain = request.POST['project_domain']
        project_description = request.POST['project_description']
        reg_no_1 = request.POST['reg_no_1']
        if len(reg_no_1) > 8:
            messages.error(request, 'Register Number be 8 digits long.')
            return redirect('project-details-1')
        student_1_no = request.POST['student_1_no']
        if len(student_1_no) > 10:
            messages.error(request, 'Number must of 10 digits.')
            return redirect('project-details-1')

        student_1_name = curr_user.first_name + ' ' + curr_user.last_name
        student_1_email = curr_user.email

        user = User.objects.get(username=curr_user.username)
        print("TYPE OF user.id: ", type(user.id))

        if Temp_Team.objects.filter(reg_no_1=reg_no_1).exists():
            messages.error(
                request, 'The Register Number already exists in another team.')
            return redirect('project-details-1')

        temp_team = Temp_Team.objects.create(project_name=project_name, project_domain=project_domain, project_description=project_description,
                                             no_of_members='1', reg_no_1=reg_no_1, student_1_name=student_1_name, student_1_email=student_1_email, student_1_no=student_1_no)

        temp_team.save()

        context = {
            'user': curr_user,
            'guides': guides,
        }

        return render(request, 'GuideList/guide.html', context)
    else:
        context = {
            'user': curr_user
        }
        return render(request, '1_project_form/1_project_form.html', context)


def project_details_2(request):
    curr_user = request.user
    guides = Guide.objects.order_by('serial_no')
    student_2_email = Otp_Two.objects.filter(temp_email=curr_user.email).get()

    if Temp_Team.objects.filter(student_1_email=curr_user.email).exists():
        if Temp_Team.objects.filter(student_2_email=student_2_email.user_email).exists():
            obj = Temp_Team.objects.filter(
                student_1_email=curr_user.email).get()
            obj.delete()
    if Team.objects.filter(teamID=curr_user.username).exists():
        is_team = Team.objects.filter(teamID=curr_user.username).get()
        is_team.delete()
        is_user = User.objects.filter(username=is_team.teamID)
        is_user.delete()
        messages.info(
            request, 'Your team is removed please to the process again!!')
        return render(request, 'Login/login.html')
    if request.method == 'POST':

        project_name = request.POST['project_name']
        project_domain = request.POST['project_domain']
        project_description = request.POST['project_description']
        reg_no_1 = request.POST['reg_no_1']
        student_1_no = request.POST['student_1_no']
        if len(reg_no_1) > 8:
            messages.error(request, 'Register Number be 8 digits long.')
            return redirect('project-details-1')
        student_1_no = request.POST['student_1_no']
        if len(student_1_no) > 10:
            messages.error(request, 'Number must of 10 digits.')
            return redirect('project-details-2')

        student_1_name = curr_user.first_name + ' ' + curr_user.last_name
        student_1_email = curr_user.email

        first_name_2 = request.POST['first_name_2']
        last_name_2 = request.POST['last_name_2']
        reg_no_2 = request.POST['reg_no_2']
        student_2_no = request.POST['student_2_no']
        if len(reg_no_2) > 8:
            messages.error(request, 'Register Number be 8 digits long.')
            return redirect('project-details-2')
        student_2_no = request.POST['student_2_no']
        if len(student_2_no) > 10:
            messages.error(request, 'Number must of 10 digits.')
            return redirect('project-details-2')

        student_2_name = first_name_2 + ' ' + last_name_2

        user = User.objects.get(username=curr_user.username)
        print("TYPE OF user.id: ", type(user.id))

        if Team.objects.filter(reg_no_1=reg_no_1).exists():
            messages.error(
                request, '1st Register Number already exists in another team.')
            return redirect('project-details-2')
        elif Team.objects.filter(reg_no_2=reg_no_2).exists():
            messages.error(
                request, '2nd Register Number already exists in another team.')
            return redirect('project-details-2')

        if Team.objects.filter(student_1_no=student_1_no).exists():
            messages.error(
                request, '1st Phone Number already exists in another team.')
            return redirect('project-details-2')
        elif Team.objects.filter(student_2_no=student_2_no).exists():
            messages.error(
                request, '2nd Phone Number already exists in another team.')
            return redirect('project-details-2')

        temp_team = Temp_Team.objects.create(project_name=project_name, project_domain=project_domain, project_description=project_description, no_of_members='2', reg_no_1=reg_no_1,
                                             student_1_name=student_1_name, student_1_email=student_1_email, student_1_no=student_1_no, reg_no_2=reg_no_2,  student_2_name=student_2_name, student_2_email=student_2_email.user_email, student_2_no=student_2_no)

        temp_team.save()

        context = {
            'guides': guides,
        }

        return render(request, 'GuideList/guide.html', context)
    else:
        print('INSIDE GET REQUEST ELSE')
        context = {
            'email': student_2_email,
            'user': curr_user,
        }
        return render(request, '2_project_form/2_project_form.html', context)


def select_guide(request):

    if request.user is None:

        return HttpResponse('YOU ARE NOT ALLOWED HERE!')

    guides = Guide.objects.order_by('serial_no')
    if request.method == 'POST':

        return redirect('guide-selected')

    context = {
        'guides': guides,
    }

    return render(request, 'GuideList/guide.html', context)


def temp_team_2(request):
    user = request.user
    if request.method == 'POST':
        if Temp_Team.objects.filter(student_1_email=user.email).exists():
            temp_team = Temp_Team.objects.filter(
                student_1_email=user.email).get()
            project_name = request.POST['project_name']
            project_domain = request.POST['project_domain']
            project_description = request.POST['project_description']
            reg_no_1 = request.POST['reg_no_1']
            if len(reg_no_1) > 8:
                messages.error(request, 'Register Number be 8 digits long.')
                return redirect('project-details-1')
            student_1_no = request.POST['student_1_no']
            if len(student_1_no) > 10:
                messages.error(request, 'Number must of 10 digits.')
                return redirect('project-details-1')

            guide = request.POST['guide']
            guide_email = request.POST['guide_email']

            student_1_name = user.first_name + ' ' + user.last_name
            student_1_email = user.email

            reg_no_2 = request.POST['reg_no_2']
            if len(reg_no_2) > 8:
                messages.error(request, 'Register Number be 8 digits long.')
                return redirect('project-details-1')
            student_2_no = request.POST['student_2_no']
            if len(student_2_no) > 10:
                messages.error(request, 'Number must of 10 digits.')
                return redirect('project-details-1')

            guide = request.POST['guide']
            guide_email = request.POST['guide_email']

            student_2_name = user.first_name + ' ' + user.last_name

            if Otp_Two.objects.filter(temp_email=user.email).exists():
                student_2_email = Otp_Two.objects.filter(
                    temp_email=user.email).get()

                student_2_email = student_2_email.user_email

            temp_team.delete()

            temp_team = Temp_Team.objects.create(project_name=project_name, project_domain=project_domain, project_description=project_description, student_1_name=student_1_name, student_1_email=student_1_email,
                                                 reg_no_1=reg_no_1, student_1_no=student_1_no, student_2_name=student_2_name, student_2_email=student_2_email, reg_no_2=reg_no_2, no_of_members='2', guide=guide, guide_email=guide_email)

            if Guide.objects.filter(email=guide_email).exists():
                guide = Guide.objects.filter(email=guide_email).get()
                temp_team.save()
                context = {
                    'id': guide.serial_no,
                    'team': temp_team,
                    'user': user
                }

                if temp_team.no_of_members == '2':
                    return render(request, 'confirmation_2/confirmation.html', context)
                else:
                    return render(request, 'confirmation_1/confirmation.html', context)
            else:
                temp_team.save()
                messages.info(
                    request, 'You have not selected the guide please select!')
                return redirect('select-guide')
        else:
            return redirect('custom_page_not_found_view')


def temp_team_1(request):
    user = request.user
    if request.method == 'POST':
        if Temp_Team.objects.filter(student_1_email=user.email).exists():
            temp_team = Temp_Team.objects.filter(
                student_1_email=user.email).get()
            project_name = request.POST['project_name']
            project_domain = request.POST['project_domain']
            project_description = request.POST['project_description']
            reg_no_1 = request.POST['reg_no_1']
            if len(reg_no_1) > 8:
                messages.error(request, 'Register Number be 8 digits long.')
                return redirect('project-details-1')
            student_1_no = request.POST['student_1_no']
            if len(student_1_no) > 10:
                messages.error(request, 'Number must of 10 digits.')
                return redirect('project-details-1')

            # guide = request.POST['guide']
            # guide_email = request.POST['guide_email']

            student_1_name = user.first_name + ' ' + user.last_name
            student_1_email = user.email

            guide_inst = Guide.objects.filter(
                email=temp_team.guide_email).get()
            guide, guide_email = guide_inst.name, guide_inst.email

            temp_team.delete()

            temp_team = Temp_Team.objects.create(project_name=project_name, project_domain=project_domain, project_description=project_description, student_1_name=student_1_name,
                                                 student_1_email=student_1_email, reg_no_1=reg_no_1, student_1_no=student_1_no, no_of_members='1', guide=guide, guide_email=guide_email)

            if Guide.objects.filter(email=guide_email).exists():
                guide = Guide.objects.filter(email=guide_email).get()
                temp_team.save()
                context = {
                    'id': guide.serial_no,
                    'team': temp_team,
                    'user': user
                }

                if temp_team.no_of_members == '2':
                    return render(request, 'confirmation_2/confirmation.html', context)
                else:
                    return render(request, 'confirmation_1/confirmation.html', context)
            else:
                temp_team.save()
                messages.info(
                    request, 'You have not selected the guide please select!')
                return redirect('select-guide')
        else:
            return redirect('custom_page_not_found_view')
    else:
        temp_team = Temp_Team.objects.filter(student_1_email=user.email).get()
        guide = Guide.objects.filter(email=temp_team.guide_email).get()
        context = {
            'id': guide.serial_no,
            'guide': guide,
            'team': temp_team,
            'user': user
        }
        if temp_team.no_of_members == '2':
            return render(request, 'temp_team_2/temp_team_2.html')
        else:
            return render(request, 'temp_team_1/temp_team_1.html')


# For confirmation page


def guide_selected(request, id):

    guide_inst = Guide.objects.get(serial_no=id)
    user = request.user
    # you can get teamID from username as both are same.
    temp_team = Temp_Team.objects.get(student_1_email=user.email)

    temp_team.guide = guide_inst.name
    temp_team.guide_email = guide_inst.email
    temp_team.save()

    obj = Otp_Two.objects.filter(temp_email=user.email)

    if request.method == 'POST':

        team = Team.objects.create(project_name=temp_team.project_name, project_domain=temp_team.project_domain, project_description=temp_team.project_description, no_of_members=temp_team.no_of_members, reg_no_1=temp_team.reg_no_1, student_1_name=temp_team.student_1_name,
                                   student_1_email=temp_team.student_1_email, student_1_no=temp_team.student_1_no, reg_no_2=temp_team.reg_no_2, student_2_name=temp_team.student_2_name, student_2_email=temp_team.student_2_email, student_2_no=temp_team.student_2_no)

        team.guide = guide_inst.name
        team.guide_email = guide_inst.email
        new_username = "CSE-%03d" % (team.id)
        team.teamID = new_username
        user.username = new_username

        print("TEAM GUIDE SERIAL ID: ", team.guide)

        user.save()
        if team.no_of_members == '2':
            # send_mail(
            #     'CONFIRMATION FOR FINAL YEAR PROJECT REGISTRATION',
            #     'Hi, Thank you for registering here is your details:' + '\n\nTeam ID: ' + team.teamID + '\n\nProject Name: ' + team.project_name + '\n\nProject Description: ' + team.project_description + '\n\nGuide Name: ' + guide_inst.name + '\n\nGuide Email: ' + guide_inst.email + '\n\nNo. of members: ' + team.no_of_members + '\n\nMembers: ' + team.student_1_name + ' and '+team.student_2_name +
            #     '\n\nNow you can login with your teamID and password(The one you created earlier)',
            #     EMAIL_HOST_USER,
            #     [user.email, team.student_2_email],
            #     fail_silently=False,
            # )
            obj.delete()
            temp_team.delete()
            team.save()
            guide_inst.vacancy -= 1
            guide_inst.save()

        else:
            # send_mail(
            #     'CONFIRMATION FOR FINAL YEAR PROJECT REGISTRATION',
            #     'Hi, Thank you for registering here is your details:' + '\n\nTeam ID: ' + team.teamID + '\n\nProject Name: ' + team.project_name + '\n\nProject Description: ' + team.project_description + '\n\nGuide Name: ' + guide_inst.name + '\n\nGuide Email: ' + guide_inst.email + '\n\nNo. of members: ' + team.no_of_members + 'Members: ' + team.student_1_name +
            #     '\n\nNow you can login with your TEAMID and password(The one you created earlier)',
            #     EMAIL_HOST_USER,
            #     [user.email, ],
            #     fail_silently=False,
            # )
            team.save()
            guide_inst.vacancy -= 1
            guide_inst.save()
            temp_team.delete()
        auth.logout(request)
        # return redirect('submitted')
        return render(request, 'submitted.html')
    context = {
        # 'guide': guide_inst,
        'team': temp_team,
        'id': id,
        'user': user,
    }
    print("TEAM MEM: ", temp_team.no_of_members)
    if temp_team.no_of_members == '2':
        print('CONFIRM 2')
        return render(request, 'confirmation_2/confirmation.html', context)
    else:
        print('CONFIRM 1')
        return render(request, 'confirmation_1/confirmation.html', context)


def credits(request):
    return render(request, 'credits/credit.html')


def search(request):
    print("INSIDE SEARCH FUNCTION: ")
    queryset_list = Guide.objects.order_by('serial_no')

    if 'name' in request.GET:
        print("INSIDE GET IF")
        name = request.GET['name']
        if name:
            print("INSIDE NAME IF..")
            queryset_list = queryset_list.filter(name__icontains=name)
            print(queryset_list)
    context = {
        'guides': queryset_list,
    }

    return render(request, 'search.html', context)


def custom_page_not_found_view(request, exception):
    return render(request, "errors/404.html", {})


def my_custom_error_view(request):
    return render(request, 'errors/500.html')


def my_custom_permission_denied_view(request, exception):
    context = {
        'exception': exception
    }
    return render(request, 'errors/403.html', context)


def my_custom_bad_request_view(request, exception):
    return render(request, 'errors/400.html')
