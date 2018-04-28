from django.shortcuts import render
from django.http import HttpResponse

from .models import Toque, User


def index(request):
    allToques = Toque.objects.all()
    return render(request, 'soundFeed/index.html', {'allToques': allToques})
