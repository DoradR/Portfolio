from django.urls import path
from .views import front_page, contact_page, projects_page

urlpatterns = [
    path('', front_page, name="front_page"),
    path('contact/', contact_page, name="contact_page"),
    path('projects/', projects_page, name="projects_page"),
]