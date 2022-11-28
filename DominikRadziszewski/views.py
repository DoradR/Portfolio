from django.shortcuts import render
from .models import Contact, Post, PicturesOfPost


def front_page(request):
    pictures = PicturesOfPost.objects.order_by()
    return render(request, 'front_page.html', {'pictures': pictures})


def projects_page(request):
    posts = Post.objects.all()
    pictures = PicturesOfPost.objects.order_by('whichPost')
    return render(request, 'projects_page.html', {'posts': posts, 'pictures': pictures})


def contact_page(request):
    contact = Contact.objects.all()
    return render(request, 'contact_page.html', {'contact': contact})
