from django.shortcuts import render
from bio.models import Advisory_Comitee, Co_Principal_Investigators, Co_Investigators, Project_Personnel


def bio(request):
    x = Advisory_Comitee.objects.all()
    y = Co_Investigators.objects.all()
    z = Co_Principal_Investigators.objects.all()
    a = Project_Personnel.objects.all()


    result = []

    for i in a:
        if i.view == True:
            result.append(i)

    context = {
        "advisory_comitees": x,
        "co_investigators":y,
        "co_principal_investigators":z,
        "project_personnels":result,
    }
    return render(request, 'meet_the_team.html', context)



def Co_Principal_Investigators_bio(request, id):
    post = Co_Principal_Investigators.objects.all().filter(id = id)
    
    context = {
        "posts": post,
    }

    return render(request, 'bio.html', context)

def Co_Investigators_bio(request, id):
    post = Co_Investigators.objects.all().filter(id = id)
    
    context = {
        "posts": post,
    }

    return render(request, 'bio.html', context)

def Project_Personnel_bio(request, id):
    post = Project_Personnel.objects.all().filter(id = id)

 
    
    context = {
        "posts": post,
    }

    return render(request, 'bio.html', context)

def Advisory_Comitee_bio(request, id):
    post = Advisory_Comitee.objects.all().filter(id = id)
    
    context = {
        "posts": post,
    }

    return render(request, 'bio.html', context)
    