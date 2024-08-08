from django.http import HttpResponse
from django.shortcuts import render
from task1.forms import ContactForm
from .models import *


# Create your views here.
def main_page(requests):
    return render(requests, 'main.html', context={'title': 'Главная страница'})


def games(requests):
    games_ = Game.objects.all()
    title = 'Игры'
    dates = ['15 января', '22 января', '29 января', '5 февраля']
    releases = [f'№{i} от {date}' for i, date in enumerate(dates, start=1)]
    context = {'title': title,
               'releases': releases,
               'games': games_}

    return render(requests, 'games.html', context=context)


def cart(requests):
    title = 'Корзина'
    cart_ = 'Ваша корзина пуста'
    context = {'title': title,
               'cart': cart_}

    return render(requests, 'cart.html', context=context)


def sign_up(request):
    buyers = Buyer.objects.all()
    info = {}
    error = ''

    if request.method == 'POST':
        for key in ('username', 'balance', 'age'):
            info[key] = request.POST.get(key, '')

        if info['username'] not in [buyer.name for buyer in buyers]:
            Buyer.objects.create(name=info['username'],
                                 age=info['age'],
                                 balance=info['balance'])
        else:
            info['username'], username = None, info['username']
            error = f'Пользователь {username} уже зарегистрирован!'

    context = {'title': 'Регистрация', 'error': error, 'username': info.get('username')}
    return render(request, 'signup.html', context=context)
