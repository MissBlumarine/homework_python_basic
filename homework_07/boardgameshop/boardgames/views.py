from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import HttpRequest
from .models import Boardgame


def index(request: HttpRequest):
    context = {
        "boardgames": Boardgame.objects.order_by("pk").all()
    }
    return render(request=request, template_name="boardgames/index.html", context=context)


def details(request: HttpRequest, pk: int):
    context = {
        "boardgame": get_object_or_404(Boardgame, pk=pk)
    }
    return render(request=request, template_name="boardgames/details.html", context=context)