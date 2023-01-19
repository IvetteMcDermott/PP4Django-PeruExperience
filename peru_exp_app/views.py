from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.http import HttpResponseRedirect

from django.http import HttpResponse
from .models import PlacesList, Comment


# Create your views here.


def landing_page(request):
    return render(request, 'index.html')


class Coast(View):

    def get(self, request, *args, **kwargs):
        model = PlacesList
        data_filtered = PlacesList.objects.filter(region='Coast')
        template = "region_places.html"
        paginate_by = 6
        context = {
            'context': data_filtered
        }

        return render(request, template, context)


class Andes(View):
    def get(self, request, *args, **kwargs):
        model = PlacesList
        data_filtered = PlacesList.objects.filter(region='The Andes')
        template = "region_places.html"
        paginate_by = 6
        context = {
            'context': data_filtered
        }

        return render(request, template, context)


class Jungle(View):
    def get(self, request, *args, **kwargs):
        model = PlacesList
        data_filtered = PlacesList.objects.filter(region='Jungle')
        template = "region_places.html"
        paginate_by = 6
        context = {
            'context': data_filtered
        }

        return render(request, template, context)


class PlaceInformation(View):

    def get(self, request, slug, *args, **kwargs):
        place = PlacesList.objects.all()
        place_data = get_object_or_404(place, slug=slug)
        comments = place_data.comments.all()
        template = 'place_information.html'
        context = {
            'context': place_data,
            'comments': comments
        }

        return render(request, template, context)
