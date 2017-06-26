from django.shortcuts import render
from github3 import login
import lecturaPython
from django.http import HttpResponse
# Create your views here.
lectura= lecturaPython
def authenthicationUser():
    gh=login("robertopaz", "21santan")
    return gh
def cargarRepos():
    nombreRepos=[]
    Repos=[]
    gh=authenthicationUser()
    repositorios = [r.refresh() for r in gh.repositories()]
    for i in range(0, len(repositorios) - 1):
        Repos.append(repositorios[i].as_dict())
    print len(Repos)
    for i in range(0, len(Repos)):
        nombreRepos.append(Repos[i]['full_name'].split('/')[1])
        print nombreRepos[i]
    return nombreRepos
def datosUser():
    userObject=authenthicationUser()
    usuario = userObject.me()
    return usuario
def cargarRepo():
    return 0
def index(request):
    dataRepos=cargarRepos()
    usuario=datosUser()
    return render(request,'umlGit/index.html',{"repos":dataRepos,"userData":usuario})
def diagrama(request,nombre=None):
    repo=nombre
    print repo
    return render(request, 'umlGit/diagrama.html', {"titulo": repo})