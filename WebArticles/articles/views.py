from django.shortcuts import render
from django.http import HttpResponse
def main(request):
    return render(request, 'articles/main.html')

def article(request):
    return render(request, 'articles/article.html')

def addarticle(request):
    return HttpResponse("<h4> добавление статьи </h4>")

def editarticle(request):
    return HttpResponse("<h4> редактирование статьи  </h4>")

def authorization(request):
    return HttpResponse("<h4> вход  </h4>")

def registration(request):
    return HttpResponse("<h4> регистрация  </h4>")

