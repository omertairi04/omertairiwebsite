from django.shortcuts import render
from django.contrib import messages
from .models import Profile , Image , Posts
from .forms import sendEmail

def index(request):
    profiles = Profile.objects.all()
    posts = Posts.objects.all()
    context = {
        'profiles':profiles,
        'posts':posts
    }

    return render(request, 'index.html', context)

def viewPost(request , title):
    post = Posts.objects.get(title=title)
    post_photos = post.content_image.all()
    context = {
        'post':post,
        'post_photos':post_photos,
    }
    return render(request , 'viewPost.html', context)

def getEmail(request):
    if request.method == 'POST':
        form = sendEmail(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request , 'Your email has been sent')
        else:
            form = sendEmail()
        
    return render(request, 'getEmail.html', {'form': form})