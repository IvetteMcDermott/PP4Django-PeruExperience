from django.shortcuts import render
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import PlacesList


# Create your views here.


class LandingPage(generic.ListView):
    model = PlacesList()
    queryset = PlacesList.objects.all()
    template_name = "index.html"
    paginate_by = 6
