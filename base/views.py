import email
from multiprocessing.connection import Client
from turtle import setundobuffer, title
from django.shortcuts import render
from django.core.paginator import Paginator
from django.core.mail import send_mail

from base.models import Member, Service,Project, Testimony,Client

def indexPage(request):
    projects = Project.objects.all()[0:1]
    projectss = Project.objects.all()[1:2]

    context = {'projects': projects, 'projectss': projectss}
    return render(request, 'base/index.html', context)


def aboutPage(request):
    members = Member.objects.all()[0:3]
    clients = Client.objects.all()
    testimonies = Testimony.objects.all()[0:1]
    testimoniess = Testimony.objects.all()[1:]

    context = {'members': members, 'clients': clients, 'testimonies': testimonies, 'testimoniess': testimoniess}
    return render(request,'base/about.html', context)

def clientsPage(request):
    clients = Client.objects.all()

    context = {'clients': clients}
    return render(request, 'base/client.html', context)
    

def contactPage(request):

    if request.method == "POST":
        contact_name = request.POST.get('contact-name')
        contact_email = request.POST.get('contact-email')
        contact_message = request.POST.get('contact-message')

        context = {'contact_name': contact_name, 'contact_email': contact_email,'contact_message':contact_message }
        
        contact_message = '''
        {}

        Email: {}
        '''.format(context['contact_message'], context['contact_email'])

        send_mail(context['contact_name'], contact_message, '',['ondijotyrell@gmail.com'])

        return render(request, 'base/contact.html', context)
    else:
        return render(request, 'base/contact.html')


def galleryPage(request):
    return render(request, 'base/gallery.html')


def projectsPage(request):
    project_list = Project.objects.all().order_by('id')
    p = Paginator(project_list, 10)
    page = request.GET.get('page')

    projects = p.get_page(page)
    nums = "a"*projects.paginator.num_pages  


    context = {'projects': projects, 'nums': nums}
    return render(request, 'base/projects.html', context)


def servicesPage(request):
    services = Service.objects.all()
    context = {'services': services}

    return render(request, 'base/services.html', context)

def memberPage(request, pk):
    profile = Member.objects.get(id=pk)
    profiles = Member.objects.all()

    context = {'profiles': profiles, 'profile': profile}
    return render(request, 'base/single-member.html', context)

def sservicePage(request, pk):
    service = Service.objects.get(id=pk)
    services = Service.objects.all()

    context = {'service':service, 'services':services }
    return render(request, 'base/single-service.html', context)


def teamPage(request):
    members = Member.objects.all()[0:7]
    associates = Member.objects.all()[7:10]

    context = {'members': members, 'associates':associates}
    return render(request, 'base/team.html', context)


def testimonialsPage(request):
    testimonies = Testimony.objects.all()[0:1]
    testimoniess = Testimony.objects.all()[1:]

    context = {'testimonies': testimonies, 'testimoniess': testimoniess}
    return render(request, 'base/testimonials.html', context)

# Create your views here.
