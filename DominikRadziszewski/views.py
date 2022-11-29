from django.shortcuts import render, get_object_or_404
from .models import Contact, Post, PicturesOfPost


def front_page(request):
    pictures = PicturesOfPost.objects.order_by()
    return render(request, 'front_page.html', {'pictures': pictures})


def projects_page(request):
    posts = Post.objects.all()
    pictures = PicturesOfPost.objects.all()
    return render(request, 'projects_page.html', {'posts': posts, 'pictures': pictures})


def contact_page(request):
    contact = Contact.objects.all()
    return render(request, 'contact_page.html', {'contact': contact})


def details_of_project_page(request, id):
    post = get_object_or_404(Post, pk=id)
    picturesOfProject = PicturesOfPost.objects.filter(whichPost=post)

    if request.method == "POST":
        post.objects.filter(id)

    return render(request, 'details_of_project_page.html', {'post': post, 'picturesOfProject': picturesOfProject})
