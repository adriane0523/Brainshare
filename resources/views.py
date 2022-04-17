from django.shortcuts import render
from resources.models import File, Resource_page, Post, Bookmarks, Related_projects, Publications,  PatientStories

def resources(request):
    posts = File.objects.all()
    resources = Resource_page.objects.all()
    case_studies = Post.objects.all().order_by('order')

    context = {
        "posts": posts,
        "resources": resources,
        "cases": case_studies,
    }
    print(context)
    return render(request, "case_studies.html", context)

def resource_index(request, id):
    posts = Resource_page.objects.all().get(index=id)
  
    context = {
        "posts": posts,
    }
    print(context)
    return render(request, "resource_index.html", context)

def case_study(request, uuid):
    posts = Post.objects.all().get(uuid=uuid)
    bookmark = Bookmarks.objects.all().filter(post=posts)
    
    context = {
        "bookmarks": bookmark,
        "posts": posts,
    }
    print(context)
    return render(request, "post.html", context)

def related_projects(request):
    related_projects = Related_projects.objects.all()
    context = {
        "projects": related_projects,
     
    }

    return render(request, "related_projects.html", context)


def publications(request):
    publications = Publications.objects.all()
    context = {
        "publications":publications,
    }

    return render (request, "publications.html", context)


def delphi_index(request, uuid):
    return render(request, "delphi_index.html")

def white_papers(request):
    resources = Resource_page.objects.all()
    context = {
        "resources": resources,
    }
    return render(request, "white_papers.html", context)

def relevant_docs(request):
    return render(request, "relevant_docs.html")

def patient_stories(request):
    patientStories = PatientStories.objects.all()

    context = {
        "patientStories":patientStories,
    }
    return render(request, "patient_stories.html", context)

def patient_stories_index(request, uuid):
    patientStory = PatientStories.objects.all().get(uuid=uuid)
    context = {
        "patientStory":patientStory,
    }
    return render(request, "patient_stories_index.html",context)