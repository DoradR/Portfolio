from django.shortcuts import render, get_object_or_404
from .models import Contact, Post, PicturesOfPost, Category
import random


def front_page(request):
    pks = Post.objects.values_list('pk', flat=True)
    random_pk = random.choice(pks)
    random_post = Post.objects.get(pk=random_pk)
    pictures = PicturesOfPost.objects.all()
    contact = Contact.objects.all()
    return render(request, 'front_page.html', {'pictures': pictures, 'random_post': random_post, 'contact': contact})


def front_page_en(request):
    pks = Post.objects.values_list('pk', flat=True)
    random_pk = random.choice(pks)
    random_post = Post.objects.get(pk=random_pk)
    pictures = PicturesOfPost.objects.all()
    contact = Contact.objects.all()
    return render(request, 'front_page_en.html', {'pictures': pictures, 'random_post': random_post, 'contact': contact})


def all_projects_page(request):
    posts = Post.objects.all()
    pictures = PicturesOfPost.objects.all()
    contact = Contact.objects.all()
    return render(request, 'all_projects_page.html', {'posts': posts, 'pictures': pictures, 'contact': contact})


def all_projects_page_en(request):
    posts = Post.objects.all()
    pictures = PicturesOfPost.objects.all()
    contact = Contact.objects.all()
    return render(request, 'all_projects_page_en.html', {'posts': posts, 'pictures': pictures, 'contact': contact})


def filtered_by_website_page(request):
    posts = Post.objects.filter(categoryOfPost=Category.objects.get(nameOfCategoryPolish="Strona Internetowa"))
    pictures = PicturesOfPost.objects.all()
    contact = Contact.objects.all()
    return render(request, 'all_projects_page.html', {'posts': posts, 'pictures': pictures, 'contact': contact})


def filtered_by_website_page_en(request):
    posts = Post.objects.filter(categoryOfPost=Category.objects.get(nameOfCategoryPolish="Website"))
    pictures = PicturesOfPost.objects.all()
    contact = Contact.objects.all()
    return render(request, 'all_projects_page_en.html', {'posts': posts, 'pictures': pictures, 'contact': contact})


def filtered_by_application_page(request):
    posts = Post.objects.filter(categoryOfPost=Category.objects.get(nameOfCategoryPolish="Aplikacja Internetowa"))
    pictures = PicturesOfPost.objects.all()
    contact = Contact.objects.all()
    return render(request, 'all_projects_page.html', {'posts': posts, 'pictures': pictures, 'contact': contact})


def filtered_by_application_page_en(request):
    posts = Post.objects.filter(categoryOfPost=Category.objects.get(nameOfCategoryPolish="Web application"))
    pictures = PicturesOfPost.objects.all()
    contact = Contact.objects.all()
    return render(request, 'all_projects_page_en.html', {'posts': posts, 'pictures': pictures, 'contact': contact})


def contact_page(request):
    contact = Contact.objects.all()
    return render(request, 'contact_page.html', {'contact': contact})


def contact_page_en(request):
    contact = Contact.objects.all()
    return render(request, 'contact_page_en.html', {'contact': contact})


def details_of_project_page(request, id):
    post = get_object_or_404(Post, pk=id)
    picturesOfProject = PicturesOfPost.objects.filter(whichPost=post)
    link = post.linkToSite
    title = post.nameOfPost
    contact = Contact.objects.all()

    if request.method == "POST":
        post.objects.filter(id)

    return render(request, 'details_of_project_page.html', {'post': post, 'picturesOfProject': picturesOfProject, 'link': link, 'title': title, 'contact': contact})


def details_of_project_page_en(request, id):
    post = get_object_or_404(Post, pk=id)
    picturesOfProject = PicturesOfPost.objects.filter(whichPost=post)
    link = post.linkToSite
    title = post.nameOfPost
    contact = Contact.objects.all()

    if request.method == "POST":
        post.objects.filter(id)

    return render(request, 'details_of_project_page_en.html', {'post': post, 'picturesOfProject': picturesOfProject, 'link': link, 'title': title, 'contact': contact})
