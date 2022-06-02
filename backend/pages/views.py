from multiprocessing import context
from django.shortcuts import render

from pages.models import Guide

# Create your views here.


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
        return render(request, 'submitted.html')
    else:

        return render(request, 'aform.html')


def submitted(request):
    # return render(request, 'index.html')
    # return render(request, 'index.html')
    return render(request, 'index.html')
