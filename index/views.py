from django.shortcuts import render

from .models import Profile , Skills , Posts

def index(request):
    profiles = Profile.objects.all()

    context = {
        'profiles':profiles,
    }

    return render(request, 'index.html', context)

