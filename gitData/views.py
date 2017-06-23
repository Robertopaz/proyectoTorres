from django.shortcuts import render
from github3 import login
from django.http import HttpResponse
# Create your views here.
def authenthicationUser():
    gh=login("robertopaz", "21santan")
    return gh
def cargarRepos():
    gh=authenthicationUser()
    repositorios = [r.refresh() for r in gh.repositories()]
    return repositorios
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
    repo=request.GET.get('nombre')
    return render(request, 'umlGit/diagrama.html', {"titulo": 'GET method'})