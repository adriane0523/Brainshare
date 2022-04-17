from django.shortcuts import render
from .models import Sulton_links

def hello_world(request):
    return render(request, 'landing_page.html', {})


def about(request):
    return render(request, 'about.html', {})

def about_sulston(request):
    sulston = Sulton_links.objects.all()
    return render(request, 'aboutSulston.html', {

        "links":sulston,

    })

def about_aims(request):
    return render(request, 'aims.html', {})

def about_importance(request):
    return render(request, 'importance.html', {})

def about_modified_delphi(request):
    return render(request, 'about_MPD.html', {} )

def contact(request):
    return render(request, 'contact.html', {})

def terms_cond(request):
    return render(request, 'terms_cond.html', {})

def privacy(request):
    return render(request, 'privacy.html', {})

def citations(request):
    return render(request, 'citations.html', {})
