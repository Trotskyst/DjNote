from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect


def home_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        auth = authenticate(username=username, password=password)
        if auth is not None:
            login(request, auth)
            return HttpResponseRedirect(reverse('notes:index'))
        else:
            messages.add_message(request, messages.INFO, "Не удалось авторизоваться!")
            return HttpResponseRedirect(reverse('home'))

    if not request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return HttpResponseRedirect(reverse('notes:index'))
