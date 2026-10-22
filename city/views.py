
from django.shortcuts import render


def home(request):
    return render(request, 'city/home.html')


def news(request):
    return render(request, 'city/news.html')


def management(request):
    return render(request, 'city/management.html')


def facts(request):
    return render(request, 'city/facts.html')


def contacts(request):
    return render(request, 'city/contacts.html')


def history(request):
    return render(request, 'city/history.html')


def history_people(request):
    return render(request, 'city/history_people.html')


def history_photos(request):
    return render(request, 'city/history_photos.html')
