from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .models import Article
from .decorators import prevent_logged


class Main(ListView):
    template_name = 'articles_list.html'
    context_object_name = 'articles'
    model = Article
    
    def get_queryset(self):
        return self.model.objects.all()[:3]


@prevent_logged
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect(reverse('cms:main'))
        else:
            return redirect(reverse('cms:register'))
            
    elif request.method == 'GET':
        form = UserCreationForm()
        return render(request, 'registration/register.html', {'form': form})


@login_required
def add_article(request):
    return HttpResponse


@login_required
def edit_article(request):
    return HttpResponse
