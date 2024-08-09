from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request, 'articles/main.html')

def article(request):
    return HttpResponse("<h4> статья  </h4>")

