from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexPage, name="index"),
    path('about/' , views.aboutPage, name="about"),
    path('client/' , views.clientsPage, name="client"),
    path('contact/' , views.contactPage, name="contact"),
    path('gallery/' , views.galleryPage, name="gallery"),
    path('projects/' , views.projectsPage, name="projects"),
    path('services/' , views.servicesPage, name="services"),
    path('member/<str:pk>/' , views.memberPage, name="member"),
    path('service/<str:pk>/' , views.sservicePage, name="sservice"),
    path('team/' , views.teamPage, name="team"),
    path('testimonials/' , views.testimonialsPage, name="testimonials"),
]