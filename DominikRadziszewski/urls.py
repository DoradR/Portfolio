from django.urls import path
from .views import front_page, contact_page, \
    all_projects_page, details_of_project_page, \
    filtered_by_application_page, filtered_by_website_page, \
    front_page_en, contact_page_en, all_projects_page_en, \
    filtered_by_application_page_en, filtered_by_website_page_en, \
    details_of_project_page_en

urlpatterns = [
    path('', front_page, name="front_page"),
    path('contact/', contact_page, name="contact_page"),
    path('projects/all', all_projects_page, name="all_projects_page"),
    path('projects/application', filtered_by_application_page, name="filtered_by_application_page"),
    path('projects/website', filtered_by_website_page, name="filtered_by_website_page"),
    path('projects/all/description/<int:id>/', details_of_project_page, name="details_of_project_page"),
    path('en/', front_page_en, name="front_page_en"),
    path('en/contact/', contact_page_en, name="contact_page_en"),
    path('en/projects/all', all_projects_page_en, name="all_projects_page_en"),
    path('en/projects/application', filtered_by_application_page_en, name="filtered_by_application_page_en"),
    path('en/projects/website', filtered_by_website_page_en, name="filtered_by_website_page_en"),
    path('en/projects/all/description/<int:id>/', details_of_project_page_en, name="details_of_project_page_en"),
]