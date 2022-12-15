from django.shortcuts import render, get_object_or_404
from .models import Contact, Post, PicturesOfPost, Category
import random


def front_page(request):
    pks = Post.objects.values_list('pk', flat=True)
    random_pk = random.choice(pks)
    random_post = Post.objects.get(pk=random_pk)
    pictures = PicturesOfPost.objects.all()
    return render(request, 'front_page.html', {'pictures': pictures, 'random_post': random_post})


def all_projects_page(request):
    posts = Post.objects.all()
    pictures = PicturesOfPost.objects.all()
    return render(request, 'all_projects_page.html', {'posts': posts, 'pictures': pictures})


def filtered_by_website_page(request):
    posts = Post.objects.filter(categoryOfPost=Category.objects.get(nameOfCategory="Strona Internetowa"))
    pictures = PicturesOfPost.objects.all()
    return render(request, 'all_projects_page.html', {'posts': posts, 'pictures': pictures})


def filtered_by_application_page(request):
    posts = Post.objects.filter(categoryOfPost=Category.objects.get(nameOfCategory="Aplikacja Internetowa"))
    pictures = PicturesOfPost.objects.all()
    return render(request, 'all_projects_page.html', {'posts': posts, 'pictures': pictures})


def contact_page(request):
    contact = Contact.objects.all()
    return render(request, 'contact_page.html', {'contact': contact})


def details_of_project_page(request, id):
    post = get_object_or_404(Post, pk=id)
    picturesOfProject = PicturesOfPost.objects.filter(whichPost=post)
    link = post.linkToSite

    if request.method == "POST":
        post.objects.filter(id)

    return render(request, 'details_of_project_page.html', {'post': post, 'picturesOfProject': picturesOfProject, 'link': link})
