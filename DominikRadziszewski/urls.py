from django.urls import path
from .views import front_page, contact_page, all_projects_page, details_of_project_page, filtered_by_application_page, filtered_by_website_page

urlpatterns = [
    path('', front_page, name="front_page"),
    path('contact/', contact_page, name="contact_page"),
    path('projects/all', all_projects_page, name="all_projects_page"),
    path('projects/application', filtered_by_application_page, name="filtered_by_application_page"),
    path('projects/website', filtered_by_website_page, name="filtered_by_website_page"),
    path('projects/all/description/<int:id>/', details_of_project_page, name="details_of_project_page"),
]