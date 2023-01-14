from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.http import HttpResponse
from .models import PlacesList


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
