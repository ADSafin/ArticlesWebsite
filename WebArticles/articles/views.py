from django.shortcuts import render, redirect
from django.views import generic
from .models import Article, User
from django.contrib.auth import authenticate, login as user_login
from django.views.generic import DetailView, UpdateView


def main(request):
    articles = Article.objects.order_by('-id')[:8]
    return render(request, 'articles/main.html', {'articles': articles})


class ArticleDetailView(generic.DetailView):
    model = Article


def registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        if password == password_confirm:
            user = User.objects.create_user(username=username, password=password)
            print("User created")
            usr = authenticate(request, username=username, password=password)
            if usr is not None:
                user_login(request, user)
                return redirect('/')
            else:
                return render(request, 'articles/main.html')
    return render(request, 'articles/registration.html')


def add_article(request):
    if request.method == 'GET':
        return render(request, 'articles/add_article.html', )
    elif request.method == 'POST':

        article = Article()
        data = request.POST

        article.title = data['title']
        article.content = data['content']
        article.author = request.user
        img = request.FILES['image']
        article.img.save(img.name, img)
        article.save()
        return redirect('/')


def edit_article(request, pk):
    if request.method == 'GET':
        return render(request, 'articles/edit_article.html', {'pk': pk})
    elif request.method == 'POST':

        article = Article.objects.get(pk=pk)
        data = request.POST

        article.title = data['title']
        article.content = data['content']
        article.author = request.user
        img = request.FILES['image']
        article.img.save(img.name, img)
        article.save()
        return redirect('/')


def delete_article(request, pk):
    if request.method == 'POST':
        article = Article.objects.get(pk=pk)
        article.delete()
        return redirect('/')
